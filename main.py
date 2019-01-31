import asyncio
import tornado.web
import tornado.ioloop
from route import urls
from loguru import logger
from databases.redis import RedisPool
from tornado.options import parse_command_line


def make_app(loop):
    logger.add("logs/api.log")
    apps = tornado.web.Application(urls)
    apps.redis = RedisPool(loop=loop).get_conn()
    return apps


if __name__ == "__main__":
    try:
        logger.info("server start")
        parse_command_line()
        loop = asyncio.get_event_loop()
        app = make_app(loop)
        app.listen(8888)
        loop.run_forever()
    except KeyboardInterrupt:
        logger.info("server stop")
