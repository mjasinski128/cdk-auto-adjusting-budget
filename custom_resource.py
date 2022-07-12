from constructs import Construct
from aws_cdk import (
    aws_logs as logs,
    aws_iam as iam,
    CfnParameter
)

from aws_cdk.custom_resources import (
    AwsCustomResource,
    AwsCustomResourcePolicy
)

import actions
import logging
from time import tzname

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class MyCustomResource(Construct):

    def __init__(self, scope: Construct, id: str, budgetName, amount, email):
        super().__init__(scope, id)

        responseData = {}

        res = AwsCustomResource(
            scope=self,
            id='AWSAutoAdjResource',
            policy=AwsCustomResourcePolicy.from_statements(
                statements=[
                    iam.PolicyStatement(
                        actions=["budgets:*"],
                        resources=["*"])
                ]
            ),
            log_retention=logs.RetentionDays.INFINITE,
            on_create=self.create(budgetName, amount, email),
            on_update=self.create(budgetName, amount, email),
            on_delete=self.delete(budgetName),
            resource_type='Custom::AutoAdjBudgetResource'
        )

    def create(self, budgetName, amount, email):
        return actions.upsert_budget(budgetName, amount=int(amount), email=email)

    def delete(self, budgetName):
        return actions.delete_budget(budgetName)
