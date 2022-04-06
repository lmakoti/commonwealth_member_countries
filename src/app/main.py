# references required
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from configs.app_settings import settings
from routers import auto_include_routers as root_routers
from utils.database import DATABASE_URL
# import databases


# import databases
# import sqlalchemy
from typing import List

import os


# insantiate the db instance
# database = databases.Database(DATABASE_URL)

# sqlalchemy db model
# metadata = sqlalchemy.MetaData()

# countries = sqlalchemy.Table(
#     "countries",
#     metadata,
#     sqlalchemy.Column("iso", sqlalchemy.String, primary_key=True),
#     sqlalchemy.Column("country", sqlalchemy.String),
#     sqlalchemy.Column("region", sqlalchemy.String),
#     sqlalchemy.Column("capital", sqlalchemy.String),
#     sqlalchemy.Column("lat", sqlalchemy.Float),
#     sqlalchemy.Column("long", sqlalchemy.Float),
# )

# create the db engine
# engine = sqlalchemy.create_engine(DATABASE_URL, pool_size=3, max_overflow=0)
# metadata.create_all(engine)


# allow consuming from client apps
app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
    license_info=settings.license_info,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow requests from all origins (not production-safe)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# manage processes, start and shutdown/terminate
# @app.on_event("startup")
# async def startup():
#     await database.connect()


# # @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


root_routers(app)
