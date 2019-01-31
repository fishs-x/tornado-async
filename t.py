from loguru import logger
import sys
#
# a = 0
# b = 1
#
# # logger.add("l.log", level="WARNING", enqueue=True, backtrace=True)
# logger.bind()
#
#
# def t():
#     logger.debug("That's it, beautiful and simple logging!")
#     logger.info("info ")
#     logger.warning("warning")
#     logger.error("this is error")
#     logger.info("If you're using Python {}, prefer {feature} of course!", 3.6, feature="f-strings")
#     try:
#         b / a
#     except Exception:
#         logger.exception("err")
#
#
# logger.start()
#
# t()
# config = {
#     "handlers": [
#         {"sink": sys.stdout, "format": "{time} - {message}"},
#         {"sink": "l.log"},
#     ],
#     "extra": {"user": "someone"}
# }
# logger.configure(**config)
#
# # For libraries
# logger.disable("1111")
# logger.info("No matter added sinks, this message is not displayed")
# logger.enable("my_library")
# logger.info("This message however is propagated to the sinks")

# logger.add("x.log")
# logger.disable("my_library")
# logger.info("No matter added sinks, this message is not displayed")
# logger.enable("my_library")
# logger.info("This message however is propagated to the sinks")

import json
from schema import Optional, Schema, Use, And

# r = Schema({'name': str, Optional('age'): Use(int)}).validate({'name': 'foobar', "age": '123'})

# r1 = Schema({'name': str, Optional('age', default=18): int}).validate({'name': 'foobar'})
# print(r, r1)

# gist = '''{"description": "the description for this gist",
#             "public": true,
#             "files": {
#                 "file1.txt": {"content": "String file contents"},
#                 "other.txt": {"content": "Another file contents"}}}'''
# gist_schema = Schema(And(Use(json.loads),
#                          {Optional('description'): str,
#                           'public': bool,
#                           'files': {str: {'content': str}}}))
# gist = gist_schema.validate(gist)
# print(gist)


########################################################################
# from peewee import Model, MySQLDatabase, PrimaryKeyField, CharField, TimestampField, Field
#
# database = MySQLDatabase('blog', **{'host': 'localhost', 'password': '', 'port': 3306, 'user': 'root'})
#
#
# # database.execute()
# class BaseModel(Model):
#     id = PrimaryKeyField()
#
#     # class Meta:
#     #     database = database
#
#
# class ABC(BaseModel):
#     username = CharField(50)
#     password = CharField(50)


# ABC.create_table(True)

#############################INSERT###########################################
# id = ABC.create(username='eee', password='666') # insert
# print(id.get_id()) # 获取insert id

# u = ABC()
# u.username="xxxx"
# u.password="777"
# u.save()
# print(u.id)

#############################SELECT###########################################
# u = ABC.select().where(ABC.username == 'xxxx').first()
# u.username= "oooo"
# u.save()

#############################异步版本###########################################
# import asyncio
# import peewee
# from peewee_async import Manager, MySQLDatabase
#
# loop = asyncio.get_event_loop()
# database = MySQLDatabase('blog', **{'host': 'localhost', 'password': '', 'port': 3306, 'user': 'root'})
# objects = Manager(database, loop=loop)
#
#
# class PageBlock(peewee.Model):
#     key = peewee.CharField(max_length=40, unique=True)
#     text = peewee.TextField(default='')
#
#     class Meta:
#         database = database
#
#
# async def my_async_func():
#     user0 = await objects.create(PageBlock, key='test', text='6666')
#     user1 = await objects.get(PageBlock, id=user0.id)
#     user2 = await objects.get(PageBlock, key='test')
#     print(user1.id, user2.id)
#
#
# # loop.run_until_complete(my_async_func())
#
# for i in PageBlock.select():
#     print(i.id)

# from services import BaseService
from services.users import UserService
#
# BaseService.instance().test("1")
# print(BaseService.instance().get_name())
# print(BaseService.instance().get_name())
#
# UserService.instance().get_name()


import asyncio
# from models.users import Users
# from services.users import UserService
#
#
# async def test_register():
#     # u = await UserService.instance().execute(Users.select().limit(2).offset(0))
#     u = await UserService.instance().select()
#     for i in u:
#         print(i.name)
#
#
# for i in Users.select():
#     pass
#
# asyncio.get_event_loop().run_until_complete(test_register())


# ========================================================================================
import asyncio

# import aioredis
#
loop = asyncio.get_event_loop()
#
#
# async def go():
#     redis = await aioredis.create_redis_pool(
#         'redis://localhost', minsize=5, maxsize=10, loop=loop, encoding='utf8')
#     await redis.set('my-key', 'value')
#     val = await redis.get('my-key')
#     print(val)
#     redis.close()
#     await redis.wait_closed()
#
#


from databases.redis import RedisPool
from databases.mysql import MysqlPool

# async def go():
#     r = RedisPool()

from models.users import Users

r = Users.select().where(Users.name == 'xx1x')
print(r.name)

# loop.run_until_complete(go())
