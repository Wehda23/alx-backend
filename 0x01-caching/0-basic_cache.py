#!/usr/bin/env python3
"""
Module contains class BasicCache
"""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Caching class
    """

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None:
            return None
        return self.cache_data.get(key, None)
