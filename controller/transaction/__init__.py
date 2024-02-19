from fastapi import Request, APIRouter

from controller.transaction.model import TransactionJSON

transaction_operations = APIRouter()


@transaction_operations.post('/transactions')
async def commit_transaction(request: Request):
    from controller import financial_service

    payload = await request.json()

    _json = TransactionJSON(**payload)
    _id = financial_service.register_transaction(_json)

    return {
        'id': _id
    }


@transaction_operations.get('/transactions')
async def get_transaction(request: Request):
    from controller import financial_service

    _id = request.headers.get('Id')

    data = financial_service.read_transaction(_id)

    return data
