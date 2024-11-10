#!/usr/bin/env python3
"""5. LFU Caching
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Least Frequently Used Cache Method
    """
    def __init__(self):
        """init method
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.usage_counts = {}
        self.least_freq_used = None

    def put(self, key, item):
        """adds cache to cache data
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_counts[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.evict()
            self.cache_data[key] = item
            self.usage_counts[key] = 1

        self.update_least_freq_used()

    def get(self, key):
        """retrieves a cache data
        """
        if key is None or key not in self.cache_data:
            return None
        self.usage_counts[key] += 1
        self.update_least_freq_used()
        return self.cache_data[key]

    def evict(self):
        """check for cache data used less frequently
        """
        if not self.cache_data:
            return

        least_used = min(self.usage_counts.values())
        candidates = [k for k, v in self.usage_counts.items()
                      if v == least_used]

        if len(candidates) > 1:
            # Apply LRU policy among the candidates
            for key in self.cache_data:
                if key in candidates:
                    evict_key = key
                    break
        else:
            evict_key = candidates[0]

        print(f'DISCARD: {evict_key}')
        del self.cache_data[evict_key]
        del self.usage_counts[evict_key]

    def update_least_freq_used(self):
        """updates the number of frequency used
        """
        least_used = min(self.usage_counts.values())
        self.least_freq_used = [k for k, v in self.usage_counts.items()
                                if v == least_used]
