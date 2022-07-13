
## Auto Adjusting Budgets (CDK) ##

New feature in AWS Budgets that enables customer to define limits based on your actual spend in the past (https://aws.amazon.com/about-aws/whats-new/2022/02/auto-adjusting-budgets/).
This removes guess work and allows to easily target increase in your spend.

Cloud Formation (CFN) resource for it is expected in future but is not yet supported, we have only web console and SDKs. CFN is extensible and in this particular case we will be using Custom Resources (https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources-lambda.html).
Custom Resource is essentially a user defined construct in CFN template that is fully programmable, in order to create, update or delete this new resource it invokes an AWS Lambda function that performs all the work. This implementation uses Python SDK for AWS.


### Prerequisites ###

#### Basic #### 
* AWS CDK

#### Advanced ####
* `python3`
* `pip`
* `make`

### Usage ###

#### Basic ####

* `make install` - install python libraries and activates virtual environment

Deploy to single AWS account with AWS CLI

* `make deploy-budget EMAIL_ADDRESS=SOME_EMAIL_ADDRESS` - deploy resources using CDK
* `make remove-budget` - remove budget with all created resources


Deploy as to multiple OUs/Accounts: TBC




### Current limitations ###

* Budget name is auto-generated and can not be changed - each Budget has unique name to avoid conflicts and crashes (benefit in StackSet deployments).

* This a PoC - adjust to your requirements before deploying to production
