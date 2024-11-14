# AWS IAM User List Fetcher

This Python script connects to AWS to retrieve and display a list of IAM users using the `boto3` library. It also includes a locally defined response dictionary to test and simulate the output structure, making it useful for both AWS-connected and offline testing scenarios.

## Prerequisites

1. **AWS CLI Configuration**: Set up your AWS CLI and configure a profile. You’ll need AWS credentials with permissions to access IAM services.
2. **Boto3 Library**: Make sure to install the `boto3` library. You can install it using:
   ```bash
   pip install boto3
   ```
3. **Dateutil Library**: This script uses `dateutil` to manage time zones. Install it using:
   ```bash
   pip install python-dateutil
   ```

## Script Overview

The script performs two main tasks:
1. Connects to AWS and retrieves IAM users.
2. Uses a locally defined dictionary to test and validate output formatting without requiring a live AWS connection.

### Code Walkthrough

```python
import boto3
from datetime import datetime
from dateutil.tz import tzutc
```

- **Imports**:
  - `boto3`: AWS SDK for Python, used to interact with AWS services.
  - `datetime` and `tzutc`: Handle date and time objects with timezone info, required for the mock `response_data` dictionary.

### AWS Connection and Fetching IAM Users

```python
# Initialize a session using an AWS profile
session = boto3.Session(profile_name='dev')  # Replace 'dev' with your AWS profile name
iam = session.client('iam')

# Fetch IAM users
response = iam.list_users()
```

- `session = boto3.Session(profile_name='dev')`: Initiates an AWS session using a specific profile (`dev`). Make sure the profile is configured in your AWS CLI.
- `iam = session.client('iam')`: Establishes an IAM client to interact with the AWS Identity and Access Management (IAM) service.
- `response = iam.list_users()`: Calls the IAM service to retrieve a list of users.

### Local Response Data for Testing

To facilitate local testing, we’ve created a sample response dictionary that mimics the structure of AWS’s actual output. This can be useful if you want to test the output formatting without needing AWS connectivity.

```python
response_data = {
    'Users': [
        {
            'Path': '/',
            'UserName': 'Alice',
            'UserId': 'AID123EXAMPLE',
            'Arn': 'arn:aws:iam::123456789012:user/Alice',
            'CreateDate': datetime(2023, 1, 15, 12, 0, 0, 0, tzinfo=tzutc()),
            'PasswordLastUsed': datetime(2024, 10, 18, 12, 0, 0, 0, tzinfo=tzutc())
        },
        {
            'Path': '/',
            'UserName': 'Bob',
            'UserId': 'AID456EXAMPLE',
            'Arn': 'arn:aws:iam::123456789012:user/Bob',
            'CreateDate': datetime(2023, 2, 20, 12, 0, 0, 0, tzinfo=tzutc()),
            'PasswordLastUsed': datetime(2024, 11, 10, 12, 0, 0, 0, tzinfo=tzutc())
        },
        # Additional users would appear here
    ],
    'IsTruncated': False,
    'ResponseMetadata': {
        'RequestId': '1234abcd-5678-efgh-9101-ijklmnopqr12',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'x-amzn-requestid': '1234abcd-5678-efgh-9101-ijklmnopqr12',
            'content-type': 'application/x-amz-json-1.1',
            'content-length': '123',
            'date': 'Thu, 12 Oct 2024 12:00:00 GMT'
        },
        'RetryAttempts': 0
    }
}
```

- **Users List**: Contains dictionaries for each user (`Alice`, `Bob`) with details like `UserName`, `UserId`, `Arn`, `CreateDate`, and `PasswordLastUsed`.
- **IsTruncated**: Indicates if there are more users to fetch. `False` means this is the complete list.
- **ResponseMetadata**: Metadata related to the response, such as request ID and HTTP status code.

### Displaying User Information

```python
for user in response_data['Users']:
    print(f"UserName: {user['UserName']}, UserId: {user['UserId']}")
```

- **Looping through users**: Iterates over each user dictionary in the `Users` list of `response_data`.
- **Print Statement**: Outputs the `UserName` and `UserId` for each user in a formatted string.

### Example Output

When run, the output will look like this:

```
UserName: Alice, UserId: AID123EXAMPLE
UserName: Bob, UserId: AID456EXAMPLE
```

This allows you to quickly see each user’s `UserName` and `UserId`.

## Notes

- **AWS Profile**: Ensure the AWS profile (`dev` in this example) is correctly configured in your AWS CLI setup.
- **Offline Testing**: The locally defined `response_data` dictionary is used here for demonstration and testing without connecting to AWS.

## References

- Boto3 Documentation: [Boto3 IAM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html)

This script is ideal for DevOps tasks, providing an efficient way to list and manage IAM users programmatically in AWS.