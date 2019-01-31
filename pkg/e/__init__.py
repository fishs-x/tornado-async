from .code import *
from .msg import Msg


def get_msg_by_code(c):
    return Msg.get(c, "")
