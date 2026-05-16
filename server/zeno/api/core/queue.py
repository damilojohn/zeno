import boto3
from zeno.api.core.config import settings

def get_sqs_client():
    return boto3.client("sqs", 
                        region_name=settings.aws_region,
                        aws_access_key_id=settings.aws_access_key_id,
                        aws_secret_access_key=settings.aws_secret_key
    )