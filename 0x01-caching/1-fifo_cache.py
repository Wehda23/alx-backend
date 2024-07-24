#!/usr/bin/env python3
"""
Module contains class BasicCache
"""


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
        self.queue = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            self.queue.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard_key = self.queue.pop(0)
                del self.cache_data[discard_key]
                print("DISCARD: {}".format(key))

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
