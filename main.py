from fastapi import FastAPI, Query, HTTPException
from database.querries import get_providers_persons, get_unique_patients
from database.connector import client

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

@app.get(f"/count-unique-persons", summary="Count of unique persons in the last N days")
async def unique_persons(n_days: int = Query(..., description="Number of days to look back")):
    try:
        cnt_persons_results = get_unique_patients(client, n_days)
        return {"n_days": n_days, "unique_person_count": cnt_persons_results}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/number-providers-and-persons",
         summary="Unique numbers of providers and persons by procedure type per every date")
async def providers_and_persons(procedure_type: int = Query(..., description="Procedure type ID")):
    try:
        result = get_providers_persons(client, procedure_type)
        return {"procedure_type": procedure_type, "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
