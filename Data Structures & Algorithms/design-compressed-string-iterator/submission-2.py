class StringIterator:

    def __init__(self, compressedString: str):
        self.length = len(compressedString) 
        self.s = compressedString   
        self.count = 0     

    def next(self) -> str:
        if self.hasNext:
            self.count += 1
            return self.s[int(count)]
        

    def hasNext(self) -> bool:
        if self.count + 1 < self.length:
            return True
        return False

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
