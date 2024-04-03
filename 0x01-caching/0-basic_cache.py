#!/usr/bin/python3
""" Basic dictionary """

from Base_caching import BaseChaching


class BasicCache(BasicCaching):
    """a class BasicCache that inherits from 
    BaseCaching and is a caching system
    """
    def put(self, key, item):
        if key is not None and item is not None:
        self.cache_data[key] = item

    def get(self, key):
        return self.cache_data.get(key, None)
