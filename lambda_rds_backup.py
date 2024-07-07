import boto3
import datetime

rds = boto3.client('rds')

def lambda_handler(event, context):
    instances = rds.describe_db_instances()
    
    for instance in instances['DBInstances']:
        rds.create_db_snapshot(
            DBSnapshotIdentifier=instance['DBInstanceIdentifier'] + '-' + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M"),
            DBInstanceIdentifier=instance['DBInstanceIdentifier']
        )
