from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache_size = capacity
        self.length = 0
        self.cache = OrderedDict()
        
    def get(self, key: int) -> int:
        #print(f'trying to get key: {key}')
        try:
            if self.cache[key] >= 0:
                #print(f'key here it is {key}')
                self.cache.move_to_end(key, last=True)
                return self.cache[key]
        except KeyError:
            #print(f'key not here it was {key}')
            return -1

    def put(self, key: int, value: int) -> None:
        try:
            # key exists -> update
            if self.cache[key] >= 0:
                self.cache[key] = value
        except:
            # key doesn't exist -> ? pop and add
            if self.length < self.cache_size:
                self.length += 1
            else:
                self.cache.popitem(last=False)
            self.cache[key] = value
        self.cache.move_to_end(key, last=True)        
        #print(f'after put operation cache is {self.cache}')


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
