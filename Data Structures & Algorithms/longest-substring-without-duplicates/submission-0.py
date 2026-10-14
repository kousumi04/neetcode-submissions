class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low=0
        res=0
        freq=set()
        for high in range(len(s)):
            while s[high] in freq:
                freq.remove(s[low])
                low+=1
            freq.add(s[high])
            res=max(res, high-low+1)
        return res        