from pydantic import BaseSettings
from typing import Union
from os import getenv
import os
import urllib


# api documentation
app_description = """
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


class Settings(BaseSettings):
    app_name: str = "Commonwealth Member Countries - API"
    app_description: str = app_description
    app_version: str = "0.1.0"
    license_info = {
        "name": "Creative Commons Zero v1.0 Universal",
        "url": "https://github.com/lmakoti/fastapi_heroku_postgres-cw-members/blob/main/LICENSE",
    }

    # # herokuapp DB connection string from env variables
    host_server: Union[str, None] = getenv("host_server")
    db_server_port= urllib.parse.quote_plus(str(getenv("host_server"))) #WHAT??
    database_name: Union[str, None] = getenv("database_name")
    db_username= urllib.parse.quote_plus(str(getenv("host_server")))
    db_password = urllib.parse.quote_plus(str(getenv("db_password")))
    ssl_mode = urllib.parse.quote_plus(str(os.environ.get("ssl_mode", "prefer"))) #???
    # connection
    


settings = Settings()
