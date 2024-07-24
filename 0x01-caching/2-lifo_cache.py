#!/usr/bin/env python3
"""
Module contains class BasicCache
"""
from collections import OrderedDict

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """
    Basic Caching class implments the lifo concept
    Last in first out concept (stack)
    """

    def __init__(self):
        """
        Class Constructor
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discared, _ = self.cache_data.popitem(True)
                print("DISCARD:", discared)

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
