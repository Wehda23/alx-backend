#!/usr/bin/env python3
"""
Module contains class BasicCache
"""
from collections import OrderedDict

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    Basic Caching class implments the fifo concept
    First in firt out concept (Queue)
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
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discared, _ = self.cache_data.popitem(False)
                print("DISCARD:", discared)

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
