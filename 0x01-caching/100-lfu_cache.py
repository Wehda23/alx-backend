#!/usr/bin/env python3
"""
Module contains class BasicCache
"""
from collections import OrderedDict, Counter

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """
    Basic Caching class implments the lifo concept
    Least recently used item
    """

    def __init__(self):
        """
        Class Constructor
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = []

    def __order_items(self, mru_key):
        """
        Reorders the items in this cache based on the most
        recently used item.
        """
        max_positions = []
        mru_freq = 0
        mru_pos = 0
        ins_pos = 0
        for i, key_freq in enumerate(self.frequency):
            if key_freq[0] == mru_key:
                mru_freq = key_freq[1] + 1
                mru_pos = i
                break
            elif len(max_positions) == 0:
                max_positions.append(i)
            elif key_freq[1] < self.frequency[max_positions[-1]][1]:
                max_positions.append(i)
        max_positions.reverse()
        for pos in max_positions:
            if self.frequency[pos][1] > mru_freq:
                break
            ins_pos = pos
        self.frequency.pop(mru_pos)
        self.frequency.insert(ins_pos, [mru_key, mru_freq])

    def put(self, key, item):
        """Adds an item in the cache."""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.frequency[-1]
                self.cache_data.pop(lfu_key)
                self.frequency.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = len(self.frequency)
            for i, key_freq in enumerate(self.frequency):
                if key_freq[1] == 0:
                    ins_index = i
                    break
            self.frequency.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__order_items(key)

    def get(self, key):
        """Retrieves an item by key."""
        if key is not None and key in self.cache_data:
            self.__order_items(key)
        return self.cache_data.get(key, None)
