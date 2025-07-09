from fastapi import FastAPI
from datetime import datetime

app = FastAPI

@app.get('/')
async def root():
    return{"Informacion":"Mi primera info"}

@app.get('/')
async def root():
    return{'HORA': datetime.now()}


@app.get('/')
async def hora_pais(codigo : str):
    tz = zonas.get(codigo.upper())
    tz2 = pytz.timazone(tz)
    return datetime.now(tz2)