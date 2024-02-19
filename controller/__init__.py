import os

from data_access import DBAccess
from service import FinancialService
from service.mongo_replicaset_flavor import FinancialServiceImpl


def init_service() -> FinancialService:
    flavor = os.environ['DATA_ACCESS_FLAVOR']
    flavor = flavor.upper()

    if flavor == 'MONGODB_REPLICASET':
        accesses = [DBAccess(f"172.20.0.1{i}", 27017) for i in range(1, 9)]
        service = FinancialServiceImpl(accesses)
        return service


financial_service: FinancialService = init_service()
