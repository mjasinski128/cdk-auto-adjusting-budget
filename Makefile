
AUTO_BUDGET_AMOUNT ?= 110
EMAIL_ADDRESS ?= budget-alarms@example.com

install:
	python3 -m venv venv
	. venv/bin/activate
	pip install -r requirements.txt

deploy-budget:
	cdk deploy --parameters email=$(EMAIL_ADDRESS) --parameters amount=$(AUTO_BUDGET_AMOUNT)

remove-budget:
	cdk destroy