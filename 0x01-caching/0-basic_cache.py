
#!/usr/bin/python3
"""  Basic dictionary """
from base_caching import BaseCaching

 """ Class that inherits from BaseCaching and is a caching system
        This caching system doesn’t have limit """
class BasicCache(BaseCaching):
    def put(self, key, item):
        """assign to the dictionary"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """returnt a value linked"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
