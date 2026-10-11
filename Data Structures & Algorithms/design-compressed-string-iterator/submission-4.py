class StringIterator:

    def __init__(self, compressedString: str):
        self.s = compressedString
        self.i = 0
        self.char = " "
        self.count = 0

    def next(self) -> str:
        if not self.hasNext():
            return " "

        if self.count == 0:
            self.char = self.s[self.i]
            self.i += 1

            while self.i < len(self.s) and self.s[self.i].isdigit():
                self.count = self.count * 10 + int(self.s[self.i])
                self.i += 1

        self.count -= 1
        return self.char

    def hasNext(self) -> bool:
        return self.count > 0 or self.i < len(self.s)