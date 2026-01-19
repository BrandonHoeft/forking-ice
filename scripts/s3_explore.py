import boto3
import json
from typing import Any, Dict


def get_aws_account_id() -> str:
    """calls AWS sts get-caller-identity and returns my AWS parsed account ID.

    Returns
    -------
    str: example id '1393093803030'
    """
    sts_client = boto3.client('sts')
    return sts_client.get_caller_identity()['Account']

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

if __name__ == "__main__":

AWS_ACCOUNT_ID = get_aws_account_id()
BUCKET_NAME = f'forking-ice-{AWS_ACCOUNT_ID}'
AWS_DEFAULT_REGION = boto3.Session().region_name
