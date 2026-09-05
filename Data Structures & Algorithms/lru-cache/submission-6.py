class LRUCache:

    def __init__(self, capacity: int):
        self.have = 0
        self.capacity = capacity
        self.stack = deque()
        self.mapping = OrderedDict()
    
        


    def get(self, key: int) -> int:
        if key in self.mapping:
            
            #remove old pos of key in stack then add at the end
            self.mapping.move_to_end(key)
            
            return self.mapping[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.mapping.move_to_end(key)
            self.mapping[key] = value
        else:
            if self.capacity > self.have:
                
                self.mapping[key] = value
                self.mapping.move_to_end(key)
                self.have += 1
                
            else:
                self.mapping.popitem(last=False)
                self.mapping[key] = value
                self.mapping.move_to_end(key)
                
                
