from fastapi import Request, APIRouter

from controller.account.model import PersonJSON, AccountJSON, CardJSON

account_operations = APIRouter()


@account_operations.post('/persons')
async def register_person(request: Request):
    from controller import financial_service

    payload = await request.json()

    _json = PersonJSON(**payload)
    _id = financial_service.register_person(_json)

    return {
        'id': _id
    }


@account_operations.get('/persons')
async def get_person(request: Request):
    from controller import financial_service

    _id = request.headers.get('Id')
    data = financial_service.read_person(_id)

    return data


@account_operations.put('/persons')
async def update_person(request: Request):
    from controller import financial_service

    _id = request.headers.get('Id')

    payload = await request.json()
    _json = PersonJSON(**payload)

    _id = financial_service.update_person(_id, _json)
    return {
        'id': _id
    }


@account_operations.post('/cards')
async def register_card(request: Request):
    from controller import financial_service

    payload = await request.json()

    _json = CardJSON(**payload)
    _id = financial_service.register_card(_json)

    return {
        'id': _id
    }


@account_operations.get('/cards')
async def get_person(request: Request):
    from controller import financial_service

    _id = request.headers.get('Id')
    data = financial_service.read_card(_id)

    return data


@account_operations.put('/cards')
async def update_card(request: Request):
    from controller import financial_service

    _id = request.headers.get('Id')

    payload = await request.json()
    _json = CardJSON(**payload)

    _id = financial_service.update_card(_id, _json)
    return {
        'id': _id
    }


@account_operations.post('/accounts')
async def register_account(request: Request):
    from controller import financial_service

    payload = await request.json()

    _json = AccountJSON(**payload)
    _id = financial_service.register_account(_json)

    return {
        'id': _id
    }


@account_operations.get('/accounts')
async def get_account(request: Request):
    from controller import financial_service

    _id = request.headers.get('Id')
    data = financial_service.read_account(_id)

    return data


@account_operations.put('/accounts')
async def update_account(request: Request):
    from controller import financial_service

    _id = request.headers.get('Id')

    payload = await request.json()
    _json = AccountJSON(**payload)

    _id = financial_service.update_account(_id, _json)
    return {
        'id': _id
    }

# @account_operations.get('/persons')
# async def get_person(request: Request):
#     from controller import financial_service
#
#     _id = request.headers.get('Id')
#     data = financial_service.read_person(_id)
#
#     return data
#
#
# @account_operations.put('/persons')
# async def update_person(request: Request):
#     from controller import financial_service
#
#     _id = request.headers.get('Id')
#
#     payload = await request.json()
#     _json = PersonJSON(**payload)
#
#     _id = financial_service.update_person(_id, _json)
#     return {
#         'id': _id
#     }
#
#
# @bank_operations.post('/departments')
# async def register_department(request: Request):
#     from controller import financial_service
#
#     payload = await request.json()
#
#     _json = BankDepartmentJSON(**payload)
#     print(_json)
#     _id = financial_service.register_department(_json)
#
#     return {
#         'id': _id
#     }
#
#
# @bank_operations.put('/departments')
# async def update_department(request: Request):
#     from controller import financial_service
#
#     _id = request.headers.get('Id')
#
#     payload = await request.json()
#     _json = BankDepartmentJSON(**payload)
#
#     _id = financial_service.update_department(_id, _json)
#
#     return {
#         'id': _id
#     }
#
#
# @bank_operations.get('/departments')
# async def get_department(request: Request):
#     from controller import financial_service
#
#     _id = request.headers.get('Id')
#
#     data = financial_service.read_department(_id)
#
#     return data

