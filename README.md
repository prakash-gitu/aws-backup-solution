# AWS Backup Solution

This project automates the backup of EBS volumes, RDS instances, and S3 buckets using AWS Lambda and CloudWatch Events.

## Prerequisites

- AWS Account
- AWS CLI configured
- IAM roles with necessary permissions

## Setup

1. **Create IAM Roles and Policies**

   Attach the policy from `iam_policy.json` to the IAM role for Lambda.

2. **Deploy Lambda Functions**

   - EBS Backup: Deploy `lambda_ebs_backup.py`
   - RDS Backup: Deploy `lambda_rds_backup.py`
   - S3 Backup: Deploy `lambda_s3_backup.py`

3. **Create CloudWatch Events**

   Create CloudWatch Events to trigger the Lambda functions based on your backup schedule.

4. **Apply S3 Lifecycle Policy**

   Apply the lifecycle policy from `s3_lifecycle_policy.json` to the destination S3 bucket.

## Usage

Ensure the Lambda functions are triggered as per the schedule to automate backups.
