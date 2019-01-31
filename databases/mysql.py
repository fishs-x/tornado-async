from loguru import logger
from peewee_async import Manager
from peewee_async import PooledMySQLDatabase


class MysqlPool:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            logger.debug("init mysql pool")
            cls.conn = PooledMySQLDatabase('blog', host='localhost', password='', port=3306, user='root',
                                           max_connections=10, charset='utf8mb4')
            cls.manager = Manager(cls.conn)
            cls._instance = super(MysqlPool, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @property
    def get_conn(self):
        return self.conn

    @property
    def get_manager(self):
        return self.manager
