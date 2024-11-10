#!/usr/bin/env python3
"""1. FIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """first in first out catch memory
    management
    """
    def __init__(self):
        """init method
        """
        super().__init__()

    def put(self, key, item):
        """add cache to cache_data using
        key value pairs
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            _key = list(self.cache_data)[0]
            del self.cache_data[_key]
            print(f'DISCARD: {_key}')

    def get(self, key):
        """retrieve the value of a key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
