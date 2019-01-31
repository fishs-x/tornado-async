from peewee import Model
from loguru import logger
from peewee_async import execute
from databases import MysqlPool, RedisPool


class BaseService:
    model: Model = None
    _service = dict()

    @classmethod
    def instance(cls):
        """Method  instance
        :return: cls
        """
        instance = cls._service.get(cls.__name__, None)
        if not instance:
            instance = cls.__new__(cls)
            cls._service.setdefault(cls.__name__, instance)
        return instance

    @staticmethod
    async def execute(sql):
        return await execute(sql)

    async def insert(self, **kwargs):
        return await self.db.create(self.model, **kwargs)

    async def find_one(self, *args, **kwargs):
        try:
            return await self.db.get(self.model, *args, **kwargs)
        except self.model.DoesNotExist:
            return None
        except Exception as e:
            logger.exception(str(e))
            return None

    @property
    def db(self):
        return MysqlPool().get_manager

    @property
    def redis(self):
        return RedisPool().get_conn()
