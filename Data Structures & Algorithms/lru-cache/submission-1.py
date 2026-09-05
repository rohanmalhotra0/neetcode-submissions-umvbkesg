class LRUCache:

    def __init__(self, capacity: int):
        self.have = 0
        self.capacity = capacity
        self.stack = []
        self.mapping = {}


    def get(self, key: int) -> int:
        if key in self.mapping:
            return self.mapping[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.mapping[key] = value
        else:
            if self.capacity > self.have:
                self.mapping[key] = value
            else:
                d = self.stack.popleft()
                del self.mapping[d]
                self.mapping[key] = value
                self.stack.append(key)
