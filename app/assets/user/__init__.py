from app.assets.db import *
from app.app import *
from functools import wraps

User = database.get_collection('user')

def required_login(senha):
    @wraps(senha)
    def required():
        ...

    return required