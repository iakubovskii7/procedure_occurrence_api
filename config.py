from utils.environment import Environment


class ConfigStrategy:
    @staticmethod
    def apply() -> None:
        pass


class DevelopmentConfig(ConfigStrategy):
    @staticmethod
    def apply() -> None:
        Config.DB_MAIN = "bigquery-public-data"
        Config.SCHEME_MAIN = "cms_synthetic_patient_data_omop"
        Config.TABLE_MAIN = "procedure_occurrence"


class ProductionConfig(ConfigStrategy):
    @staticmethod
    def apply() -> None:
        Config.DB_MAIN = "bigquery-public-data"
        Config.SCHEME_MAIN = "cms_synthetic_patient_data_omop"
        Config.TABLE_MAIN = "procedure_occurrence"



class Config:
    DB_MAIN = "bigquery-public-data"
    SCHEME_MAIN = "cms_synthetic_patient_data_omop"
    TABLE_MAIN = "procedure_occurrence"

    @staticmethod
    def init() -> None:
        env = Config.detect_environment()
        strategy = {
            "stage": DevelopmentConfig,
            "production": ProductionConfig,
        }.get(env, ConfigStrategy)

        strategy.apply()

    @staticmethod
    def detect_environment() -> str:
        if Environment.IS_PROD_ENV:
            return "production"
        else:
            return "stage"


Config.init()
