from fastapi import Request
from mypy_boto3_sqs import SQSClient


def get_sqs_client(request: Request) -> SQSClient:
    return request.app.state.sqs_client
