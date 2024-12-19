from typing import Literal

from fastapi import FastAPI, Query, HTTPException
from pydantic import PositiveInt, ValidationError

from app.database.querries import get_providers_persons, get_unique_patients
from app.database.connector import client
from app.models.models import UniquePersonsResponse, ProvidersAndPersonsResponse



app = FastAPI(
    title="Procedure Occurrence API",
    description="API to analyze procedure_occurrence data from BigQuery",
    version="1.0.0"
)



@app.get("/")
async def root():
    return {"message": f"Hello! This is REST API service for procedure_occurrence data. "
                       f"We have two endpoints: "
                       f"/count-unique-persons and /number-providers-and-persons"
            }

@app.get(f"/count-unique-persons",
         response_model=UniquePersonsResponse,
         summary="Count of unique persons in the last N days"
         )
async def unique_persons(n_days: PositiveInt = Query(default=7, ge=1, description="Number of days to look back")):
    try:
        cnt_persons_results = get_unique_patients(client, n_days)
        return {"n_days": n_days, "unique_person_count": cnt_persons_results}
    except ValidationError as e:
        raise HTTPException(status_code=422,
                            detail=str(e))
    except Exception as another_errors:
        raise HTTPException(status_code=400, detail=str(another_errors))

@app.get("/number-providers-and-persons",
         response_model=ProvidersAndPersonsResponse,
         summary="Unique numbers of providers and persons by procedure type per every date")
async def providers_and_persons(procedure_type: PositiveInt = Query(default=38000251,
                                                                                    description="Procedure type ID")):
    if procedure_type not in [38000251, 38000269]:
        raise HTTPException(status_code=422,
                            detail=f"Procedure type {procedure_type} not supported. "
                                   f"Please, choose from 38000251, 38000269")
    try:
        result = get_providers_persons(client, procedure_type)
        return {"procedure_type": procedure_type, "data": result}

    except Exception as another_errors:
        raise HTTPException(status_code=400, detail=str(another_errors))
