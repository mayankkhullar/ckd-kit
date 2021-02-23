from aws_cdk import core
from aws_cdk import aws_config as config
from aws_cdk import aws_s3 as s3


class App2Stack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        #bucket = s3.Bucket(self, id='s3cdkbucket',bucket_name='config-212467762323',versioned=True)
        recorder = config.CfnConfigurationRecorder(self, id='recorder', role_arn='arn:aws:iam::212467762323:role/aws-service-role/config.amazonaws.com/AWSServiceRoleForConfig',recording_group=None)
        channel = config.CfnDeliveryChannel(self, id='channel', s3_bucket_name='config-212467762323')
        srule = config.CfnConfigRule(self, id='rule1', source=config.CfnConfigRule.SourceProperty(owner="AWS",source_identifier="REQUIRED_TAGS"),
                input_parameters={"tag1Key":"tagVal"})
        srule2 = config.CfnConfigRule(self, id='rule2', source=config.CfnConfigRule.SourceProperty(owner="AWS",source_identifier="S3_BUCKET_LEVEL_PUBLIC_ACCESS_PROHIBITED"))
