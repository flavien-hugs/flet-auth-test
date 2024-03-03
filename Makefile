ifneq (,$(wildcard .env))
    include .env
    export
endif


.PHONY: help
help:	## Show this help
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: run
startapp: ## Run service
	poetry run app

.PHONY: pre-commit
pre-commit: ## Run pre-commit
	pre-commit run --all-files
