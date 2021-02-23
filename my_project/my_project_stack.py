from aws_cdk import core
from aws_cdk import aws_s3 as s3


class MyProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, id='s3cdkbucket',bucket_name='udemy-cdk-9440-6371-0048',versioned=True)

        # The code that defines your stack goes here
