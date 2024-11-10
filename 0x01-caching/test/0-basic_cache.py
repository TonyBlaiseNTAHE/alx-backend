#!/usr/bin/env python3
"""0. Basic dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching

def BasicCache(BaseCaching):
    """0. Basic dictionary
    """
    def put(self, key, item):
        """creates key-value pair
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """get item of a particular key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
