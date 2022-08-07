from aws_cdk import Stack, aws_ec2, aws_memorydb
from constructs import Construct


class SearchHistoryPocStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
