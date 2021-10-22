# Makefile for dockerizing the application and running helm install 
# helm install is used to deploy into a kubernetes cluster 

APP_NAME=revolutapi
VERSION=v1

.PHONY: build
build: build  ## dockerise the simple http api python app 
	docker build -t $(APP_NAME):$(VERSION) . 

# Deploy the dockerised app into minikube using helm chart 
.PHONY: install
install: install
	cd revolutchart && \
	helm upgrade --install revolutchart revolutapi/ -f revolutapi/values.yaml --set image.tag=${VERSION}

	

# Run the test 
.PHONY: test
test: test
	python3 tests/tests.py -v 