from pydantic import BaseModel

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
