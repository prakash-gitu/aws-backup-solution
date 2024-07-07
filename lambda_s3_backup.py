import boto3

s3 = boto3.client('s3')

SOURCE_BUCKET = 'source-bucket-name'
DEST_BUCKET = 'destination-bucket-name'

def lambda_handler(event, context):
    objects = s3.list_objects_v2(Bucket=SOURCE_BUCKET)
    
    for obj in objects.get('Contents', []):
        copy_source = {'Bucket': SOURCE_BUCKET, 'Key': obj['Key']}
        s3.copy_object(CopySource=copy_source, Bucket=DEST_BUCKET, Key=obj['Key'])
