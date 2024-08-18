import logging  # use for error reporting and debugging
import os

import boto3  # AWS SDK for python
from botocore.exceptions import ClientError  # Error handling for AWS services
import argparse  # command line parsing


def show_menus():
    """
    Display the menu options to the user.
    """
    print("\nMenu:")
    print("1. Create bucket")
    print("2. List buckets")
    print("3. Upload files")
    print("4. Delete files")
    print("5. Delete bucket")
    print("6. Exit")


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
            s3_client = boto3.client('s3', region_name=region)
            location = {
                'LocationConstraint': region}  # needed when creating s3 buckets outside of default region 'us-east-1'
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def delete_bucket(bucket_name):
    """
    Delete an s3 bucket. The bucket must be empty before it can be deleted.
    :param bucket_name: bucket to delete.
    :return: True if bucket was deleted, False otherwise
    """
    s3_client = boto3.client('s3')

    try:
        # Delete the contents of the bucket first
        objects = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in objects:
            for obj in objects['Contents']:
                s3_client.delete_object(Bucket=bucket_name, key=obj['Key'])

            # Deleting empty bucket
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted'.")
        return True
    except ClientError as e:
        print(f"Error deleting bucket '{e}'")
        return False


def list_buckets():
    """
    List all s3 buckets
    :return: list of bucket names
    """
    s3_client = boto3.client('s3')
    response = s3_client.list_buckets()
    return [bucket['Name'] for bucket in response['Buckets']]


def upload_file(file_name, bucket_name, object_name=None):
    """
    Upload file to s3 bucket
    :param file_name: file to upload
    :param bucket_name: bucket to upload to
    :param object_name: s3 object name. If not provided, use file_name
    :return: True if upload succeeded, else False
    """

    # If s3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def delete_object(bucket_name, object_key):
    """
    Delete an object from a s3 bucket.
    :param bucket_name: bucket to delete from
    :param object_key: name of object to delete
    :return: True if object was deleted, else False
    """
    s3_client = boto3.client('s3')

    try:
        s3_client.delete_object(Bucket=bucket_name, Key=object_key)
        print(f"Object '{object_key}' deleted from bucket '{bucket_name}'")
    except ClientError as e:
        print(f"Error deleting object: {e}")
        return False
    return True

