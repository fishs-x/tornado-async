from loguru import logger
from services import BaseService
from models.users import Users


class UserService(BaseService):
    model = Users

    async def get(self):
        await self.redis.set('mm', 'gg')
        # 增
        res = await self.insert(name='888')
        logger.debug("增--> {}, {}".format(res.id, res.name))
        # 查
        res = await self.find_one(name='888')

        logger.debug("查-->{}, {}".format(res.id, res.name))
        # 改
        res.name = 'xxx'
        await self.db.update(res)

    async def test_transaction(self):
        """
        需要捕获异常
        同步peewee Example::
            :try
                with db.atomic() as transaction:
                    Users.create(name='123xxx')
                    Users.create(name='234xxx234xxx234xxx234xxx234xxx234xxx234xxx234xxx234xxx234xxx234xxx234xxx234xxx234xxx')
            :except
                :return None
        :return:
        """
        try:
            async with self.db.atomic():
                await self.db.create(self.model, name='123xxx')
                await self.db.create(self.model, name='1')
        except Exception as e:
            logger.exception(str(e))