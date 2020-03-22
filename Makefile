.DEFAULT_GOAL := help

install-reqs: ## pip install requirements
	pip install -r requirements.txt

install-reqs-test: ## pip install requirements for tests
	pip install -r requirements-test.txt

install-reqs-all: ## pip install all requirements
	pip install -r requirements.txt
	pip install -r requirements-test.txt

test: ## run tests
	pytest -sv .

help: ## show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
