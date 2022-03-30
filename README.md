# Building an API (fastAPI, Heroku & PostgreSQL)
> Building an API for Commonwealth member countries, filter results by all member countries, by region and by ISO3 Code as identified from <a href="https://www.iban.com/country-codes" target="_blank">iban</a>

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
or go to <a href="https://fastapi-heroku-postgres-cw.herokuapp.com" target="_blank">https://fastapi-heroku-postgres-cw.herokuapp.com</a>

- `/region/[specify_region]` - returns all member countries in a region, region values are `Africa, Americas, Asia, Europe or Pacific`

## Credit

Much appreciation and credit goes to `Tse'po Melvin Thoabala` for pointing me in the right direction and `Navule Pavan Kumar Rao` @tutlinks for the amazing tutorial: <a href="https://www.tutlinks.com/fastapi-with-postgresql-crud-async/" target="_blank">https://www.tutlinks.com/fastapi-with-postgresql-crud-async/</a>

## Connect
Lets connect on LinkedIn: <a href="https://www.linkedin.com/in/lehlohonolomakoti/" target="_blank">Lehlohonolo Makoti</a> <br/>
Learn more: <a href="https://lmakoti.codepool.tech" target="_blank">Portfolio</a> <br/>
GitHub: <a href="https://github.com/lmakoti/" target="_blank">https://github.com/lmakoti</a>

