# Implement REST API service for procedure_occurrence data


## Task

The goal of this project is to implement a RESTful API that provides analytical insights based on the procedure_occurrence table from the public BigQuery cms_synthetic_patient_data_omop dataset.

## Data

Use public BigQuery dataset cms_synthetic_patient_data_omop.procedure_occurrence

## Functionality

1. Implement an endpoint that returns the count of unique persons for the last N procedure_dat.
2. Implement an endpoint that returns the total number of unique providers and persons for a specified procedure type, grouped by procedure_dat.


## Requirements
1. Python web framework
2. Swagger documentation
3. Code is modular and bug-free
4. Service should be deployed using Docker

[Optional] Basic error reporting


## Hints
Instruction for authenticating with Google Cloud services in a docker container - https://cloud.google.com/run/docs/testing/local#docker-with-google-cloud-access

# Solution
1. Clone repository
2. Build docker image:
docker build -t procedure_occurrence -f Dockerfile .
3. First way to run dockerfile using the following command:

   docker run -p 8080:8080 \ 
      -e K_SERVICE=dev \
      -e K_CONFIGURATION=dev \
      -e K_REVISION=dev-00001 \
      -e GOOGLE_APPLICATION_CREDENTIALS=/tmp/keys/[file_json_credentials].json \
      -v $GOOGLE_APPLICATION_CREDENTIALS:/tmp/keys/[file_json_credentials].json:ro \
       procedure_occurrence

4. Second way to run

gcloud beta code dev --dockerfile=Dockerfile --service-account=[your_service_account_mail] --local-port=8080

5. Swagger documentation is located on /docs endpoint
