class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros=0
        ones=0
        twos=0
        for i in nums:
            if i==0:
                zeros+=1
            elif i==1:
                ones+=1    
            else:
                twos+=1
        nums.clear()
        for i in range(zeros):
            nums+=[0]
        for i in range(ones):
            nums+=[1]
        for i in range(twos):
            nums+=[2]
        return nums            

