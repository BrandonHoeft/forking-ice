import boto3
import json
from typing import Any, Dict


def create_s3_bucket(bucket_name: str, region: str) -> None:
    """create a new s3 bucket

    Parameters
    ----------
    bucket_name: something likely to be unique to avoid global S3 name conflict
    region: e.g. 'us-east-2' or 'us-west-1'
    """
    # Create an S3 client
    s3_client = boto3.client('s3', region_name=region)

    # Create the S3 bucket
    try:
        s3_client.create_bucket(Bucket=bucket_name)
        print(
            f"S3 bucket '{bucket_name}' created successfully in region '{region}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

## TODO: download request from moneypuck.com

## TODO: upload_file_to_s3()

if __name__ == "__main__":

    AWS_ACCOUNT_ID = boto3.client('sts').get_caller_identity()['Account']  # to use as unique id part in new s3 bucket
    BUCKET_NAME = f'forking-ice-{AWS_ACCOUNT_ID}'
    AWS_DEFAULT_REGION = boto3.Session().region_name

    create_s3_bucket(BUCKET_NAME, AWS_DEFAULT_REGION)
    print(boto3.client('s3').list_buckets())  # aka `aws s3 ls`
