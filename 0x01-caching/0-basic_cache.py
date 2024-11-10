#!/usr/bin/env python3
"""0. Basic dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache
    """
    def put(self, key, item):
        """Add an item to the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data
        linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
