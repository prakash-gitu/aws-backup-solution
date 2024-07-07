import boto3
import datetime

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    volumes = ec2.describe_volumes()
    
    for volume in volumes['Volumes']:
        ec2.create_snapshot(
            VolumeId=volume['VolumeId'],
            Description='Automated snapshot - ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
