from models.users import Users
from databases import MysqlPool

db = MysqlPool().get_conn


with db.atomic() as transaction:
    Users.create(name='123xxx')
    Users.create(name='234xxx')
