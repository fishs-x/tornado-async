from databases.mysql import MysqlPool
from peewee import Model, PrimaryKeyField


class BaseModel(Model):
    id = PrimaryKeyField()

    class Meta:
        # table_name = 'users'
        database = MysqlPool().get_conn
        legacy_table_names = False
