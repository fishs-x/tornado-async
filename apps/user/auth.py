from loguru import logger
from apps import BaseHandler
from services.users import UserService


class LoginHandler(BaseHandler):
    async def post(self):
        """用户登陆"""
        v = await self.redis.get('my-key')
        logger.debug(v)
        # users = await UserService.instance().get()
        users = await UserService.instance().test_transaction()
        self.response(users)


class RegisterHandler(BaseHandler):
    def post(self):
        """用户注册"""
        pass


class ForgotPasswordHandler(BaseHandler):
    def put(self):
        """忘记密码"""
        pass


class ResetPasswordHandler(BaseHandler):
    def put(self):
        """重制密码"""
        pass
