.DEFAULT_GOAL := test

.PHONY: clean detect_missing_migrations help requirements test validate quality production-requirements migrate static clean_static

# Generates a help message. Borrowed from https://github.com/pydanny/cookiecutter-djangopackage.
help: ## Display this help message
	@echo "Please use \`make <target>\` where <target> is one of"
	@perl -nle'print $& if m{^[\.a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

deploy: deploy.web deploy.api

deploy.api:

	heroku container:login
	cd api; heroku container:push web -a save-backend
	heroku container:release web -a save-backend


deploy.web:

	heroku container:login
	cd client; heroku container:push web -a save-frontend
	heroku container:release web -a save-frontend
