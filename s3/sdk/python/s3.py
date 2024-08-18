import logging
import boto3
from botocore.exceptions import ClientError


def create_bucket(bucket_name, region='us-west-1'):
    """
    Create s3 bucket in the specified region
    Default region will be us-west-1
    :param bucket_name: bucket that will be created
    :param region: pass region to work with
    :return: True if bucket was created successfully, else False
    """
    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True
