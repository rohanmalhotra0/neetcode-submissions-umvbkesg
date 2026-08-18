class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        print("".join(res))
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        if s == []:
            return ""
        res, i, j = [] , 0, 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1 
            
            length = int(s[i:j])
            i = j + 1

            res.append(s[i:i + length])
            i += length
            '''
            if s[i] in "0123456789":
                res.append(str(s[i+2:i+2+int(s[i])]))
                i += int(s[i])+ 2
            '''
        return res