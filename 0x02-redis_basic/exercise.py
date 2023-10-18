#!/usr/bin/env python3
""" Module is an introduction to Redis as a DB manager and for caching """
from redis import Redis
from typing import Union, Callable, Optional
from uuid import uuid4


class Cache:
    """ Implements a Redis client to be used for caching operations """
    # def __init__(self, count: Union[None, Callable] = None):
    def __init__(self) -> None:
        """ Initialises the class with default properties """
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Adds some data to the cache """
        key = uuid4().__str__()
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[str, bytes, int, float, None]:
        """ Gets a value and deserializes it to desired format using fn """
        # count_calls(self)
        value = self._redis.get(key)
        if fn and value:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """ Converts bytes to a string """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """ Converts bytes to an integer """
        return self.get(key, int)


# @Cache
# # def count_calls(self, func: Callable) -> Callable:
# def count_calls(self, method: Callable) -> Callable:
#     """ Count times methods of the Cache class are called """
#     # self._redis.incr(self.__qualname__)
#     # return self._redis.get(self.__qualname__)
#     self._redis.incr(method.__qualname__)
#     return self._redis.get(method.__qualname__)


# if __name__ == '__main__':
#     """ Tests the code in this module """
#     # r = Redis()
#     # x = r.set('key', 'Hello world!')
#     # print(x, type(x))
#     # x = r.get('key')
#     # print(x, type(x))
#     # x = r.get('null')
#     # print(x, type(x))
#
#     cache = Cache()
#     # #                 Task 0
#     # data = b'hello'
#     # key = cache.store(data)
#     # print(key)
#     # local_redis = Redis()
#     # print(local_redis.get(key))
#
#     # #                   Task 1
#     # TEST_CASES = {
#     #     b'foo': None,
#     #     123: int,
#     #     'bar': lambda d: d.decode('utf-8')
#     # }
#     # for value, fn in TEST_CASES.items():
#     #     key = cache.store(value)
#     #     assert cache.get(key, fn=fn) == value
#     #     val = cache.get(key, fn=fn)
#     #     print(key, ' => ', value, type(value), ' >> ', val, type(val),
#     #           f'[{fn}]{type(fn)}')
#     # # Tests the new methods: get(), get_str(), and get_int()
#     # print()
#     # k = cache.store(234)
#     # m = cache.get(k)
#     # print('cache.get() without fn parameter:', m, type(m))
#     # m = cache.get(k, str)
#     # print('cache.get() with fn=str parameter:', m, type(m))
#     # m = cache.get_str(k)
#     # print('cache.get_str():', m, type(m))
#     # m = cache.get_int(k)
#     # print('cache.get_int():', m, type(m))
#
#     # #                   Task 2
#     # def milk_s():
#     #     pass
#     # print(milk_s.__qualname__)
#     # cache.store(b"first")
#     # print(cache.get(cache.store.__qualname__))
#     #
#     # cache.store(b"second")
#     # cache.store(b"third")
#     # print(cache.get(cache.store.__qualname__))
#
#     # #                   Task 3
#     # s1 = cache.store("first")
#     # print(s1)
#     # s2 = cache.store("secont")
#     # print(s2)
#     # s3 = cache.store("third")
#     # print(s3)
#     #
#     # inputs = cache._redis.lrange(
#     #     "{}:inputs".format(cache.store.__qualname__), 0, -1)
#     # outputs = cache._redis.lrange(
#     #     "{}:outputs".format(cache.store.__qualname__), 0, -1)
#     #
#     # print("inputs: {}".format(inputs))
#     # print("outputs: {}".format(outputs))
