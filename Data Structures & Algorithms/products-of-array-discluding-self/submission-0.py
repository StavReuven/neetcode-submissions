class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*len(nums)
        post = [1]*len(nums)
        sum = 1
        output = [1]*len(nums)
        for i in range(0,len(nums)):
            pre[i] = sum
            sum = sum*nums[i]
        sum = 1
        for i in range(len(nums) - 1,-1,-1):
            post[i] = sum
            sum = sum*nums[i]

        for i in range(0,len(nums)):
            output[i] = pre[i] * post[i]
        
        return output