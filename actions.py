import boto3
from datetime import datetime, timezone
import logging
from botocore.exceptions import ClientError

from aws_cdk.custom_resources import (
    AwsSdkCall,
    PhysicalResourceId
)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('budgets')
AccountId = boto3.client('sts').get_caller_identity().get('Account')


def focm():
    today = datetime.now()
    first = today.replace(day=1, hour=0, minute=0,
                          second=0, tzinfo=timezone.utc)
    firstDayOfCurrMonth = first
    return firstDayOfCurrMonth


def create_budget(name, email, amount, unit='PERCENTAGE', method='EMAIL'):
    print("Create "+name+' '+email)
    return AwsSdkCall(
        service="Budgets",
        action="createBudget",
        physical_resource_id=PhysicalResourceId.of("Id"),
        parameters={
            "AccountId": AccountId,
            "Budget": {
                'BudgetName': name,
                'TimeUnit': 'MONTHLY',
                'TimePeriod': {
                    'Start': focm(),
                    'End': datetime(2030, 1, 1, tzinfo=timezone.utc)
                },
                'BudgetType': 'COST',
                'LastUpdatedTime': focm(),
                'AutoAdjustData': {
                    'AutoAdjustType': 'HISTORICAL',
                    'HistoricalOptions': {
                        'BudgetAdjustmentPeriod': 1,
                    },
                }
            },
            "NotificationsWithSubscribers": [
                {
                    'Notification': {
                        'NotificationType': 'FORECASTED',
                        'ComparisonOperator': 'GREATER_THAN',
                        'Threshold': amount,
                        'ThresholdType': unit,
                        'NotificationState': 'ALARM',
                    },
                    'Subscribers': [
                        {
                            'SubscriptionType': method,
                            'Address': email
                        },
                    ]
                },
            ]
        })


def delete_budget_api(name):
    if get_budget(name) == None:
        return

    response = client.delete_budget(
        AccountId=AccountId,
        BudgetName=name
    )
    return response


def delete_budget(name):

    if get_budget(name) == None:
        return

    print("Delete "+AccountId+' '+name)
    return AwsSdkCall(
        service="Budgets",
        action="deleteBudget",
        parameters={
            "AccountId": AccountId,
            "BudgetName": name
        })


def upsert_budget(name, email, amount, unit='PERCENTAGE', method='EMAIL'):
    if get_budget(name) == None:
        print('Create budget '+name)
        return create_budget(name, email, amount, unit, method)
    else:
        print('Replace budget '+name)
        delete_budget_api(name)
        return create_budget(name, email, amount, unit, method)


def get_budget(name):
    print('get budget '+name)
    try:
        response = client.describe_budget(
            AccountId=AccountId,
            BudgetName=name
        )
        return response.get('Budget')

    except ClientError as e:
        if e.response['Error']['Code'] == 'NotFoundException':
            return None
