
## Auto Adjusting Budgets (CDK) ##

New feature in AWS Budgets that enables customer to define limits based on your actual spend in the past (https://aws.amazon.com/about-aws/whats-new/2022/02/auto-adjusting-budgets/).
This removes guess work and allows to easily target increase in your spend.

Cloud Formation (CFN) resource for it is expected in future but is not yet supported, we have only web console and SDKs. This project make use of CDK and Python SDK to help create budget resources.


### Prerequisites ###

* `AWS CDK cli` 
* `python3`
* `pip`
* `make`

### Usage ###

#### Basic ####

* `make install` - install python libraries and activates virtual environment

Deploy to single AWS account with AWS CLI

* `make deploy-budget EMAIL_ADDRESS=SOME_EMAIL_ADDRESS AUTO_BUDGET_AMOUNT=SOME_PERCENTAGE` - deploy resources using CDK (`AUTO_BUDGET_AMOUNT=110` for `110%` trigger)
* `make remove-budget` - remove budget with all created resources


Deploy to multiple OUs/Accounts: TBC




### Current limitations ###

* Budget name is auto-generated and can not be changed - each Budget has unique name to avoid conflicts and crashes (benefit in StackSet deployments).

* This a PoC - adjust to your requirements before deploying to production
