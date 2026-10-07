class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        m = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            m[bill] += 1
            if bill > 5:
                x = bill - 5 
                if x == 5:
                    if m[5] >= 1:
                        m[5] -= 1
                        continue
                    return False 
                else:
                    if m[5] >= 1 and m[10] >= 1:
                        m[10] -= 1
                        m[5] -= 1
                        continue 
                    if m[5] >= 3:
                        m[5] -= 3
                        continue
                    return False
        return True