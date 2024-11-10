#!/usr/bin/env python3
"""1. FIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """First In First Out
    """
    def __init__(self):
        """init class
        """
        super().__init__()

    def put(self, key, item):
        """assigns to the dictionary
        self.cache_data the item value
        for the key key
        """
        if key is None or item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            _key = list(self.cache_data)[0]
            self.cache_data.pop(_key)
            print(f'DISCARD: {_key}')
            self.cache_data[key] = item

        def get(self, key):
            """get value of key
            """
            if key is None or key not in self.cache_data:
                return None
            return self.cache_data[key]
