class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low=0
        res=float('inf')
        windowSum=0
        for high in range(len(nums)):
            windowSum+=nums[high]
            while windowSum>=target:
                res=min(res, high-low+1)
                windowSum-=nums[low]
                low+=1
        if res==float("inf"):
            return 0
        else:
            return res            