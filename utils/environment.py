import os

class Environment:
    IS_PROD_ENV = os.getenv("IS_PROD_ENV") == 'true'