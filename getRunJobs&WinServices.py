import pyodbc
import subprocess
import argparse
from datetime import datetime, timedelta

# SQL Server connection details
server = 'localhost'  # Replace with your SQL Server hostname or IP address
port = '1433'         # Replace with the port number (e.g., 1433)
database = 'msdb'     # The database name (for SQL Server Agent job history)
username = 'sa'       # Replace with your SQL Server username
password = 'YourPassword123!'  # Replace with your SQL Server password

# Define the connection string with the port
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server},{port};DATABASE={database};UID={username};PWD={password}'

# Function to connect to SQL Server
def connect_sql():
    connection = None
    cursor = None
    try:
        connection = pyodbc.connect(conn_str)
        cursor = connection.cursor()
        print("Connected to SQL Server successfully.")
        return cursor, connection
    except Exception as e:
        print(f"Error: {e}")
        exit()

# Function to search for running jobs in SQL Server
def search_running_jobs(cursor):
    """Search for jobs that are currently running."""
    query = f"""
        SELECT job_id, run_status, run_date, run_duration, message
        FROM msdb.dbo.sysjobhistory
        WHERE run_status = 4  -- 4 means Running
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

def format_run_date(run_date, run_duration):
    """Format the run date and run duration into a human-readable format."""
    # Convert run_date from int (YYYYMMDD) to datetime
    run_date_str = str(run_date)
    run_date_formatted = datetime.strptime(run_date_str, '%Y%m%d')

    # Convert run_duration from int (HHMMSS) to timedelta
    hours = run_duration // 10000
    minutes = (run_duration % 10000) // 100
    seconds = run_duration % 100
    run_duration_formatted = timedelta(hours=hours, minutes=minutes, seconds=seconds)

    return run_date_formatted, run_duration_formatted

def print_job_details(rows):
    """Print job details."""
    if rows:
        for row in rows:
            run_date_formatted, run_duration_formatted = format_run_date(row.run_date, row.run_duration)
            print(f"Job ID: {row.job_id}")
            print(f"Run Status: {'Running' if row.run_status == 4 else 'Not Running'}")
            print(f"Run Date: {run_date_formatted.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Run Duration: {run_duration_formatted}")
            print(f"Message: {row.message}")
            print("-" * 50)
    else:
        print("No running jobs found.")

# Function to get services in batches with filtering by status and DisplayName search pattern
def get_services_batch(batch_size=500, offset=0, status=None, search_pattern=None):
    try:
        # Modify the PowerShell command to filter by status and display name search pattern if provided
        filters = []
        if status:
            filters.append(f"Where-Object {{ $_.Status -eq '{status}' }}")
        if search_pattern:
            filters.append(f"Where-Object {{ $_.DisplayName -like '*{search_pattern}*' }}")

        filter_command = " | ".join(filters)
        filter_command = f" | {filter_command}" if filter_command else ""

        # Start the PowerShell process to get a subset of services with filters
        process = subprocess.Popen(
            ["powershell", "-Command", f"Get-Service {filter_command} | Select-Object -Skip {offset} -First {batch_size}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Read the output and errors
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            # Return output if no error occurs
            return stdout.splitlines()
        else:
            print(f"Error occurred: {stderr}")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Function for automatic pagination and displaying services in chunks
def paginate_services(batch_size=500, status=None, search_pattern=None):
    offset = 0
    while True:
        # Get the next batch of services
        services = get_services_batch(batch_size=batch_size, offset=offset, status=status, search_pattern=search_pattern)

        if not services:  # If no services are returned (empty or error), break
            print("No more services or an error occurred.")
            break

        # Display the current batch of services
        print(f"\nDisplaying services starting from service {offset + 1} to {offset + len(services)}:")
        for service in services:
            print(service)

        # Move to the next batch
        offset += batch_size  # Increment the offset for the next batch

# Main function to execute
def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Get services in batches with status and search pattern filters.")
    
    # Argument for selecting the mode (SQL Server job or services)
    parser.add_argument("--mode", choices=["sql", "services"], required=True, help="Mode of operation: 'sql' for SQL Server job, 'services' for Windows services")
    
    # Argument for SQL Server
    parser.add_argument("--running", action="store_true", help="Search for jobs that are currently running in SQL Server.")
    
    # Arguments for Windows services
    parser.add_argument("--status", choices=["running", "stopped"], help="Filter services by status")
    parser.add_argument("--search_pattern", type=str, help="Search services by DisplayName (using 'like' pattern)")
    parser.add_argument("--batch_size", type=int, default=500, help="Number of services to fetch per batch")

    # Parse arguments
    args = parser.parse_args()

    if args.mode == "sql":
        # SQL Server mode
        cursor, connection = connect_sql()
        
        if args.running:
            print("Searching for running jobs:")
            running_jobs = search_running_jobs(cursor)
            print_job_details(running_jobs)

        # Close the SQL Server connection
        cursor.close()
        connection.close()

    elif args.mode == "services":
        # Windows services mode
        paginate_services(batch_size=args.batch_size, status=args.status, search_pattern=args.search_pattern)

if __name__ == "__main__":
    main()
