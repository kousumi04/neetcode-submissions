class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low=0
        res=0
        maxFreq=0
        count={}
        for high in range(len(s)):
            count[s[high]]=count.get(s[high], 0)+1
            maxFreq=max(maxFreq, count[s[high]])
        
            while(high-low+1)-maxFreq>k:
                count[s[low]]-=1
                low+=1
            res=max(res, high-low+1)
        return res    