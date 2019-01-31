import json
import tornado.web
from peewee import Model
from pkg.e import get_msg_by_code, code
from services import JwtCipher, set_dict
from schema import Schema
from aioredis import Redis
from playhouse.shortcuts import model_to_dict


class BaseHandler(tornado.web.RequestHandler):
    user = None
    _json_args = None

    def data_received(self, chunk):
        pass

    @property
    def redis(self) -> Redis:
        return self.application.redis

    def auth_user(self) -> bool:
        """判断用户是否登陆
        :return bool
        """
        token = self.request.headers.get("Authentication")
        user_info = JwtCipher.decrypt(token)
        if not user_info:
            return False
        self.user = set_dict(user_info)
        return True

    def get_json_args(self, key=None, default=None):
        """获取json数据
        :return dict or val
        """
        try:
            if self._json_args is None:
                self._json_args = json.loads(self.request.body)
            if key is None:
                return self._json_args
            if default:
                return self._json_args.get(key, default)
            return self._json_args[key]
        except json.JSONDecodeError:
            raise tornado.web.HTTPError(400)

    def is_valid(self, schema: Schema, data=None):
        """表单验证"""
        if not data:
            data = self.get_json_args()
        return schema.is_valid(data)

    def response(self, data=None, c=None):
        """统一返回消息"""
        if not data:
            data = dict()
        elif isinstance(data, Model):
            data = model_to_dict(data)
        c = c or code.SUCCESS
        data = json.dumps(dict(code=c, data=data, msg=get_msg_by_code(c)))
        self.write(data)


class AuthHandler(BaseHandler):
    def prepare(self):
        if not self.auth_user():
            raise tornado.web.HTTPError(401)
