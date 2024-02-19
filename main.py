

import logging
import os

import uvicorn
from fastapi import FastAPI

os.environ['DATA_ACCESS_FLAVOR'] = 'MONGODB_REPLICASET'

from controller.bank import bank_operations

logging.basicConfig(level=logging.DEBUG)


api = FastAPI()
api.include_router(bank_operations)

if __name__ == "__main__":
    uvicorn.run("main:api", host="0.0.0.0", port=6001, reload=False)
