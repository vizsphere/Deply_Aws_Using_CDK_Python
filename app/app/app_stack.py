from aws_cdk import (
    # Duration,
    Stack,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_s3 as s3
)
from constructs import Construct

class AppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "cdk_speakers_2025",
                encryption=s3.BucketEncryption.KMS
            )

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "AppQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
