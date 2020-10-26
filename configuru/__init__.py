"""Top-level package for configuru."""

__author__ = """robotnaoborot"""
__email__ = 'robotnaoborot@gmail.com'
__version__ = '0.1.1'

import os, inspect, re


class Config:
    def __init__(self):
        if os.path.exists('.env'):
            with open('.env', 'r') as f:
                for line in map(str.strip, f):
                    line = re.match(r'''(.*)=['"]?([^"']+)"?$''', line)
                    if line:
                        key, value = line.groups()
                        key = key.upper()
                        if key not in os.environ:
                            os.environ[key] = value
        for key, value in inspect.getmembers(self):
            if key.startswith("_") or key not in self.__annotations__:
                continue
            var_type = self.__annotations__[key]
            if hasattr(var_type, '__origin__':
                    var_type = var_type.__origin__
            setattr(
                self, key, var_type(os.environ.get(key.upper(), value))
            )

__all__ = ['Config', '__author__', '__email__', '__version__']
