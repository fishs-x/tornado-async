from .base import BaseService
from .common import JwtCipher

import itertools


class Row(dict):
    """A dict that allows for object-like property access syntax."""

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)


def set_dict(data) -> Row:
    return Row(itertools.zip_longest(data.keys(), data.values()))
