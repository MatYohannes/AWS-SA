from constructs import Construct
from aws_cdk import (
    Stack,
    aws_s3 as s3,
)


class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a s3 bucket
        s3.Bucket(self, "MyBucket")

