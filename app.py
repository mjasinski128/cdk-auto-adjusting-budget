from aws_cdk import (
    App, Stack,
    CfnParameter,
    Names
)

from custom_resource import MyCustomResource


class MyStack(Stack):
    def __init__(self, scope: App, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        amount = CfnParameter(self,
                              "amount",
                              type='Number'
                              )

        email = CfnParameter(
            self,
            "email"
        )

        resource = MyCustomResource(
            self, "AutoAdjustingBudgetCDK",
            budgetName="AutoAdjustingBudgetCDK"+Names.unique_id(amount),
            amount=amount.value_as_number,
            email=email.value_as_string
        )


app = App()
MyStack(app, "AutoAdjustingBudget")
app.synth()
