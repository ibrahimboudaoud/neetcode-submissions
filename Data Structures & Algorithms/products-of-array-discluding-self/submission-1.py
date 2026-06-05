class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for i in range(len(nums))]

        pre = 1
        for i in range(1, len(nums)):
            output[i] *= nums[i-1] * output[i-1]
        
        post =1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= post
            post *= nums[i]
                


       

        return output
        