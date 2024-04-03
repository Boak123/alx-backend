#!/usr/bin/env python3
""" class FIFOCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
