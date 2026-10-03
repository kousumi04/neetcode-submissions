class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        res, majority=0,0
        for n in nums:
            freq[n]=freq.get(n, 0)+1
            if freq[n]>majority:
                res=n
                majority=freq[n]
        return res        
