from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_s3 as s3,
    aws_lambda as lambada_,
    aws_lambda_event_sources as lambda_event_sources
)
from constructs import Construct

class AppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "cdkspeakers2025",
            encryption=s3.BucketEncryption.KMS,
            bucket_name="cdkspeakers2025"
        )
        
        queue = sqs.Queue(self, "SqsLambdaDemoQueue",
            visibility_timeout=Duration.seconds(300)
        )

        sqs_lambda = lambada_.Function(self, "SQSLambda",
                    handler='lambda_handler.handler',
                    runtime=lambada_.Runtime.PYTHON_3_9,
                    code = lambada_.Code.from_asset('lambda')
        )

        #Create event source : https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_lambda_event_sources/README.html
        sqs_event_source = lambda_event_sources.SqsEventSource(queue)
        # Add SQS event source to lambad 
        sqs_lambda.add_event_source(sqs_event_source)