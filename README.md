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
3. Run dockerfile using the following command:

docker run -p 8000:8000 \ 
   -e K_SERVICE=dev \
   -e K_CONFIGURATION=dev \
   -e K_REVISION=dev-00001 \
   -e GOOGLE_APPLICATION_CREDENTIALS=[path_to_json_credentials] \
   -v $GOOGLE_APPLICATION_CREDENTIALS:[path_to_json_credentials]:ro \
    procedure_occurrence

