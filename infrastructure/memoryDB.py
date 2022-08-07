from aws_cdk import Stack, CfnOutput, CfnParameter, aws_memorydb
from constructs import Construct


class MemoryDBAclStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        MEMORYDB_USER_NAME = CfnParameter(
            self,
            "MemoryDBUserName",
            type="String",
            description="memory db user name",
            default="memdb-admin",
        )

        MEMORYDB_USER_PASSWORD = CfnParameter(
            self,
            "MemoryDBUserPassword",
            type="String",
            description="memory db user password (16~128 printable characters)",
        )

        memorydb_user = aws_memorydb.CfnUser(
            self,
            "MemoryDBUser",
            user_name=MEMORYDB_USER_NAME.value_as_string,
            # refer to https://redis.io/topics/acl
            access_string="on ~* &* +@all",
            # refer to https://docs.aws.amazon.com/cli/latest/reference/memorydb/create-user.html
            authentication_mode={
                "Type": "password",
                "Passwords": [MEMORYDB_USER_PASSWORD.value_as_string],
            },
        )

        self.memorydb_acl = aws_memorydb.CfnACL(
            self,
            "MemoryDBAcl",
            acl_name="my-memorydb-acl",
            user_names=[memorydb_user.user_name],
        )

        CfnOutput(
            self,
            "MemoryDBACL",
            value=self.memorydb_acl.acl_name,
            export_name="MemoryDBACL",
        )
