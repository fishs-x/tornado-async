import jwt
import time
from .config import JWT_KEY


class JwtCipher:
    @classmethod
    def encrypt(cls, user_id) -> str:
        """
        根据id 生成token
        :param user_id: 用户id
        """
        data = {"user_id": user_id, "login_time": time.time()}
        return jwt.encode(data, JWT_KEY, algorithm='HS256').decode()

    @classmethod
    def decrypt(cls, token) -> dict:
        """
        解锁token内信息
        :param token:
        """
        try:
            return jwt.decode(token, JWT_KEY)
        except Exception:
            return {}
