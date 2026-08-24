from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        curr = collections.deque()
        for ch in s:
            if ch not in seen:
                curr.append(ch)
                seen.add(ch)
            else:
                curr.append(ch)
                curr.popleft()
           
        return len(curr)