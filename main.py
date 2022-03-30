# references required
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import starlette.responses as response
import databases
import sqlalchemy
from typing import List
import urllib
import os

#api documentation
description = """
## Overview

**Technology Stack Documentation** 

1. **Github**: <a href="https://docs.github.com/en" target="_blank">https://docs.github.com/en</a>

2. **FastAPI**: <a href="https://fastapi.tiangolo.com/" target="_blank">https://fastapi.tiangolo.com</a>

3. **Heroku**: <a href="https://devcenter.heroku.com/categories/reference" target="_blank">https://devcenter.heroku.com/categories/reference</a>

4. **PostgreSQL**: <a href="https://www.postgresql.org/docs/" target="_blank">https://www.postgresql.org/docs</a>

## Solution Architecture

1. Create a project repository on GitHub and add: python gitignore and creative commons licence
2. Create a Heroku app and link it to the project repo
3. Create the database on Heroku and obtain the connection credentials
4. Using any postgres client (DBeaver) connect to the database and import the member countries' data into a new table
5. Create the fastAPI code to build the API.

## Using the api

**Base URL**: `https://fastapi-heroku-postgres-cw.herokuapp.com/`

**Endpoints**:

- `/countries` - returns all member countries
- `/iso/[specify_iso3]` - returns a single member country based ISO3 code, to see codes run:

```php
curl -X GET "https://fastapi-heroku-postgres-cw.herokuapp.com/countries" -H "accept: application/json"
```
or go to <a href="https://fastapi-heroku-postgres-cw.herokuapp.com/countries" target="_blank">https://fastapi-heroku-postgres-cw.herokuapp.com/countries</a>

- `/region/[specify_region]` - returns all member countries in a region, region values are `Africa, Americas, Asia, Europe or Pacific`

## Credit

Much appreciation and credit goes to `Ts'epo Melvin Thoabala` for pointing me in the right direction and `Navule Pavan Kumar Rao` @tutlinks for the amazing tutorial: <a href="https://www.tutlinks.com/fastapi-with-postgresql-crud-async/" target="_blank">https://www.tutlinks.com/fastapi-with-postgresql-crud-async/</a>

## Connect
Lets connect on LinkedIn: <a href="https://www.linkedin.com/in/lehlohonolomakoti/" target="_blank">Lehlohonolo Makoti</a> <br/>
Learn more: <a href="https://lmakoti.codepool.tech" target="_blank">Portfolio</a> <br/>
GitHub: <a href="https://github.com/lmakoti/" target="_blank">https://github.com/lmakoti</a>

"""

# herokuapp DB connection string from env variables
host_server = os.environ['host_server']
db_server_port = urllib.parse.quote_plus(str(os.environ['db_server_port']))
database_name = os.environ['database_name']
db_username = urllib.parse.quote_plus(str(os.environ['db_username']))
db_password = urllib.parse.quote_plus(
    str(os.environ['db_password']))
ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode', 'prefer')))
# connection
DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host_server, db_server_port,
                                                               database_name, ssl_mode)

# insantiate the db instance
database = databases.Database(DATABASE_URL)

# sqlalchemy db model
metadata = sqlalchemy.MetaData()

countries = sqlalchemy.Table(
    "countries",
    metadata,
    sqlalchemy.Column("iso", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("country", sqlalchemy.String),
    sqlalchemy.Column("region", sqlalchemy.String),
    sqlalchemy.Column("capital", sqlalchemy.String),
    sqlalchemy.Column("lat", sqlalchemy.Float),
    sqlalchemy.Column("long", sqlalchemy.Float),
)

# create the db engine
engine = sqlalchemy.create_engine(
    DATABASE_URL, pool_size=3, max_overflow=0
)
metadata.create_all(engine)


# create pydantic models
class CountryJson(BaseModel):
    # iso3: str
    country: str
    region: str
    capital: str
    lat: float
    long: float

class Country(BaseModel):
    iso: str
    country: str
    region: str
    capital: str
    lat: float
    long: float


# allow consuming from client apps
app = FastAPI(title="Commonwealth Member Countries - API", description=description, version="0.1",
        license_info={
        "name": "Creative Commons Zero v1.0 Universal",
        "url": "https://github.com/lmakoti/fastapi_heroku_postgres-cw-members/blob/main/LICENSE",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow requests from all origins (not production-safe)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# manage processes, start and shutdown/terminate
@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/')
def index():
    return response.RedirectResponse("/docs")

#return all member countries
@app.get("/countries/", response_model=List[Country])
async def get_member_countries():
    query = countries.select()
    return await database.fetch_all(query)

# return a single member country
@app.get("/iso/{country_iso}", response_model=Country, status_code = status.HTTP_200_OK)
async def get_member_country_filter(country_iso: str):
    query = countries.select().where(countries.c.iso == country_iso)
    return await database.fetch_one(query)

#return all member countries in a particular region
@app.get("/region/{region}", response_model=List[Country])
async def get_members_in_region(region: str):
    query = countries.select().where(countries.c.region == region)
    return await database.fetch_all(query)

