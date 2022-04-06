from fastapi import APIRouter, status
from schemas.country import Country
# from main import database

router = APIRouter(
    tags=["API - Country"], responses={404: {"description": "Not Found"}}
)


# return all member countries
@router.get("/countries/")
#  response_model=List[Country]
async def get_member_countries():
    return {"back": "new life"}
    # query = countries.select()
    # return await database.fetch_all(query)

# not sure I like this
# @app.get("/")
# def index():
#     return response.RedirectResponse("/docs")


# return a single member country
@router.get("/iso/{country_iso}", response_model=Country, status_code=status.HTTP_200_OK)
async def get_member_country_filter(country_iso: str):
    return {"back": "bass"}
    # query = countries.select().where(countries.c.iso == country_iso)
    # return await database.fetch_one(query)


# # return all member countries in a particular region
# @app.get("/region/{region}", response_model=List[Country])
# async def get_members_in_region(region: str):
#     return {"back": "bass"}
#     # query = countries.select().where(countries.c.region == region)
#     # return await database.fetch_all(query)
