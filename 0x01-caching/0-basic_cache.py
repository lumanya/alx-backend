#!/usr/bin/env python3
""" Create a class BasicCache that inherits from BaseCaching and is a caching
system:
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ inherit BaseCaching class """

    def put(self, key, item):
        """ assign to the dictionary self.cache_data the item  value of the key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data  linked to key """
        key = self.cache_data.get(key)
        return None if key is None else key
