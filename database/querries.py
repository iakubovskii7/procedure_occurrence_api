from config import Config
from utils.environment import Environment
import datetime
table_ref = f"{Config.DB_MAIN}.{Config.SCHEME_MAIN}.{Config.TABLE_MAIN}"


def create_query_for_unique_patients(n: int) -> str:
      """
      Create query for GBQ to get count of unique persons for the last N procedure_dat.
      """
      query_unique_patients = f"""
          with n_unique_dats as (
            select distinct procedure_dat
            from `bigquery-public-data.cms_synthetic_patient_data_omop.procedure_occurrence`
            order by procedure_dat desc
          )

          select count(distinct person_id) as cnt_persons
          from f"{Config.DB_MAIN}.{Config.SCHEME_MAIN}.{Config.TABLE_MAIN}"
          inner join (select procedure_dat from n_unique_dats limit {n}) using(procedure_dat)
      """
      return query_unique_patients

def get_query_providers_persons(procedure_type_concept_id: int) -> str:
    query = f"""
            select 
                    procedure_dat,
                    count(distinct provider_id) as cnt_providers,
                    count(distinct person_id) as cnt_persons
            from `bigquery-public-data.cms_synthetic_patient_data_omop.procedure_occurrence`
            where procedure_type_concept_id = {procedure_type_concept_id}  -- 38000251, 38000269
            group by procedure_dat
            order by procedure_dat
            """
    return query


def get_unique_patients(client, n_days: int) -> int:
      """
      Get unique patients count for the last N procedure_dat.
      :param client: Bigquery client connection
      :param n_days: integer value for last N days
      :return: integer unique patients numbers
      """
      if Environment.IS_STAGE:
            cnt_persons_results = 12242
      else:
            query_job = client.query(create_query_for_unique_patients(n_days))
            cnt_persons_results = int(query_job.to_dataframe()['cnt_persons'].values[0])

      return cnt_persons_results


def get_providers_persons(client, procedure_type_concept_id: int) -> dict[datetime.date, dict[str, int]]:
    """
    Create nested dictionary for total number of unique providers and persons for a specified procedure type, grouped by procedure_dat.
    :param client: Bigquery client connection
    :param procedure_type_concept_id: integer value for procedure type
    :return: nested dictionary; first key - date; second key - dictionary where key is providers or persons
    Example of returned dictionary: {datetime.date(2007, 11, 27): {'cnt_providers': 5, 'cnt_persons': 5}}
    """
    if Environment.IS_STAGE:
          nested_dict = {datetime.date(2007, 11, 27): {'cnt_providers': 5, 'cnt_persons': 5}}
    else:
          query = get_query_providers_persons(procedure_type_concept_id)
          query_job = client.query(query)
          nested_dict = {}

          for row in query_job:
              procedure_date = row['procedure_dat']
              nested_dict[procedure_date] = {
                  "cnt_providers": row['cnt_providers'],
                  "cnt_persons": row['cnt_persons']
              }
    return nested_dict
