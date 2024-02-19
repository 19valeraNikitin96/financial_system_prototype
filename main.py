import logging
import os

import uvicorn
from fastapi import FastAPI


os.environ['DATA_ACCESS_FLAVOR'] = 'MONGODB_REPLICASET'


from controller.bank import bank_operations
from controller.account import account_operations
from controller.transaction import transaction_operations


logging.basicConfig(level=logging.DEBUG)


api = FastAPI()
api.include_router(bank_operations)
api.include_router(account_operations)
api.include_router(transaction_operations)

if __name__ == "__main__":
    uvicorn.run("main:api", host="0.0.0.0", port=6001, reload=False)
