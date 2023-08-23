#!/usr/bin/python3
from base_caching import BaseCaching

class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()  # Call the parent class's __init__() method
        self.access_history = []  # To track the access history of cache items

    def put(self, key, item):
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.access_history.remove(key)  # Remove the key from access history

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Find the least recently used item (LRU)
            lru_key = self.access_history[0]
            print("DISCARD:", lru_key)

            del self.cache_data[lru_key]  # Remove the LRU item from cache
            self.access_history.pop(0)  # Remove the LRU key from access history

        self.cache_data[key] = item
        self.access_history.append(key)  # Add the key to the end of access history

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        self.access_history.remove(key)  # Remove the key from access history
        self.access_history.append(key)  # Add the key to the end of access history

        return self.cache_data[key]
