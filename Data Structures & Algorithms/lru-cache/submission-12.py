class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if key == self.cache[i][0]:
                temp = self.cache.pop(i)
                val = temp[1]
                self.cache.append(temp)
                return val
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if key == self.cache[i][0]:
                temp = self.cache.pop(i)
                temp[1] = value
                self.cache.append(temp)
                return
        
        if len(self.cache) == self.capacity:
            self.cache.pop(0)
        
        self.cache.append([key, value])
        return
