import os

class Environment:
    IS_PROD_ENV = os.getenv("IS_PROD_ENV") == 'true'
    IS_STAGE = os.getenv("IS_STAGE") == 'true'