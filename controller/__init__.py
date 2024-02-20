import os

from service import FinancialService
from service.autumndb_flavor import FinancialServiceImpl as AutumnDBFinancialServiceImpl
from service.mongo_replicaset_flavor import FinancialServiceImpl as ReplicasetFinancialServiceImpl
from service.tc_flavor import FinancialServiceImpl as TCFinancialServiceImpl


def init_service() -> FinancialService:
    flavor = os.environ.get('DATA_ACCESS_FLAVOR', None)
    if flavor is None:
        return None

    flavor = flavor.upper()

    if flavor == 'MONGODB_REPLICASET':
        service = ReplicasetFinancialServiceImpl()
        return service

    if flavor == 'TC':
        service = TCFinancialServiceImpl()
        return service

    if flavor == 'AUTUMN':
        service = AutumnDBFinancialServiceImpl()
        return service


financial_service: FinancialService = init_service()
