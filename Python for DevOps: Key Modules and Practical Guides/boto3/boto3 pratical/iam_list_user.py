import boto3
from datetime import datetime
from dateutil.tz import tzutc


#session = boto3.Session(profile_name='dev')  # Use the profile you configured
#iam = session.client('iam')

#response = iam.list_users()

# Store the response data in a variable testing locally with output
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


for user in response_data['Users']:
    print(f"Users:{user['UserName']}, userId:{user['UserId']}")

print(f"IsTruncated: {response_data['IsTruncated']}")

# Print HTTPStatusCode from ResponseMetadata
print(f"HTTPStatusCode: {response_data['ResponseMetadata']['HTTPStatusCode']}")
