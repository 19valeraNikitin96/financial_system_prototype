from fastapi import Request, APIRouter

from controller.bank.model import ATMJSON, BankDepartmentJSON

bank_operations = APIRouter()


@bank_operations.post('/atms')
async def register_atm(request: Request):
    from controller import financial_service

    payload = await request.json()

    _json = ATMJSON(**payload)
    print(_json)
    _id = financial_service.register_atm(_json)

    return {
        'id': _id
    }


@bank_operations.get('/atms')
async def get_atm(request: Request):
    from controller import financial_service

    _id = request.headers.get('Id')
    print(_id)

    data = financial_service.read_atm(_id)

    return data


@bank_operations.put('/atms')
async def update_atm(request: Request):
    from controller import financial_service

    _id = request.headers.get('Id')

    payload = await request.json()
    _json = ATMJSON(**payload)

    _id = financial_service.update_atm(_id, _json)

    return {
        'id': _id
    }


@bank_operations.post('/departments')
async def register_department(request: Request):
    from controller import financial_service

    payload = await request.json()

    _json = BankDepartmentJSON(**payload)
    print(_json)
    _id = financial_service.register_department(_json)

    return {
        'id': _id
    }


@bank_operations.put('/departments')
async def update_department(request: Request):
    from controller import financial_service

    _id = request.headers.get('Id')

    payload = await request.json()
    _json = BankDepartmentJSON(**payload)

    _id = financial_service.update_department(_id, _json)

    return {
        'id': _id
    }


@bank_operations.get('/departments')
async def get_department(request: Request):
    from controller import financial_service

    _id = request.headers.get('Id')

    data = financial_service.read_department(_id)

    return data

# @bank_operations.post('/departments')
# async def create(request: Request):
#     payload = await request.json()
#
#
#     return {
#         'id': _id
#     }
#
#
# @bank_operations.put(_path)
# async def update(request: Request):
#     _id = request.headers.get('Id')
#     payload = await request.json()
#
#
#     return {
#         'id': _id
#     }
#
#
# @bank_operations.get(_path)
# async def read(request: Request):
#     _id = request.headers.get('Id')
#
#
#     return data
