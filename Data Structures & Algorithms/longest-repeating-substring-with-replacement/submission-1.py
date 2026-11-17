class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        c={}
        res=0
        maxf=0
        for right in range(len(s)):
            c[s[right]]=c.get(s[right], 0)+1
            maxf=max(maxf, c[s[right]])
            while (right-left+1)-maxf>k:
                c[s[left]]-=1
                left+=1
            res=max(res, right-left+1)
        return res    
