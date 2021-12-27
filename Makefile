.DEFAULT_GOAL := help
.PHONY: 

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
activate:  ## Activate scripts
	chmod u+x ./scripts/set_pythonpath.sh 
	./scripts/set_pythonpath.sh
