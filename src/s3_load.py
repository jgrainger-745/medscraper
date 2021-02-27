import boto3


s3 = boto3.resource(
    service_name ='s3',
    #region = 'us-east-2',
    aws_access_key_id='AKIATA54LMTGBT4YV5NA',
    aws_secret_access_key='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',
)


for bucket in s3.buckets.all():
    print(bucket.name)