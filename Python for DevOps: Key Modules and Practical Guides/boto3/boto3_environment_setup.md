# Boto3 Environment Setup

## Overview

In this tutorial, we'll set up our AWS environment to work with Boto3 by configuring AWS credentials. This includes using the **AWS Command Line Interface (AWS CLI)** to manage AWS services and automate tasks.

---

## What is AWS CLI?

The **AWS Command Line Interface (AWS CLI)** is a unified tool that enables you to manage your AWS services from the command line. With a single installation, you can control multiple AWS services, simplifying automation tasks through scripts.

- **Download AWS CLI**: Follow the [AWS CLI installation guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) to set up the CLI on your machine.

---

## Setting Up AWS Credentials

### Step 1: Create a New IAM User in AWS

1. **Log in** to the [AWS Management Console](https://aws.amazon.com/console/).
2. Go to **IAM Console** and select **Users**.
3. Create a new user with **Programmatic access**.
4. Attach the **AdministratorAccess** policy to the user.
5. Download the **Access Key ID** and **Secret Access Key** provided for this user.

### Step 2: Configure AWS CLI with Credentials

To configure your credentials for AWS CLI, use the following commands.

#### Configure Default Profile

Running the following command will set up a **default profile**:
```bash
aws configure
```

#### Configure Multiple Profiles

To set up separate profiles for different environments (e.g., development, QA, production), use:
```bash
aws configure --profile dev
aws configure --profile qa
aws configure --profile prod
```

When prompted, enter your **Access Key ID**, **Secret Access Key**, **Region**, and **Output format** for each profile.

---

## First Automation Script: List IAM Users

Let’s create a script to list all IAM users in your AWS account using Boto3.

### Manual Steps

1. **Log in** to the [AWS Management Console](https://aws.amazon.com/console/).
2. Go to the **IAM Console**.
3. In the IAM Console, you’ll find various options such as:
   - **Users**
   - **Groups**
   - **Roles**
   - **Policies**

### Automation Script

To list IAM users programmatically, use this code in a Python script:

```python
import boto3

# Initialize a session using Amazon IAM
session = boto3.Session(profile_name='dev')  # Use the profile you configured
iam = session.client('iam')

# List all IAM users
response = iam.list_users()
for user in response['Users']:
    print(f"User: {user['UserName']}")
```

For more code examples and detailed explanations, check out the [GitHub repository](https://github.com/CodeNinjaOps/python_projects.git).

---

With these steps, you've successfully set up your AWS environment for Boto3 and are ready to automate AWS tasks! In the next tutorials, we’ll explore additional Boto3 functions and scripts to manage other AWS services.