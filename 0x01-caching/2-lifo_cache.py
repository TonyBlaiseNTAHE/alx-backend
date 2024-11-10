#!/usr/bin/env python3
"""2. LIFO Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """class LIFOCache
    """
    def __init__(self):
        """init class
        """
        super().__init__()
        self.last_key_added = None

    def put(self, key, item):
        """assign item to key in a dictionary
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS\
                and key not in self.cache_data:

            if self.last_key_added:
                print(f'DISCARD: {self.last_key_added}')
                del self.cache_data[self.last_key_added]

        self.cache_data[key] = item
        self.last_key_added = key

    def get(self, key):
        """retrieves the value of the key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
