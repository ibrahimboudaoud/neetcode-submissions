class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for i in range(len(nums))]

        left= {}
        right = {}
        sol = [0 for i in range(len(nums))]

        left[0] = 1
        right[len(nums)-1] = 1

        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        
        for i in range(len(nums) - 2, -1, -1):
            right [i] = right[i+1] * nums[i+1]

        for i in range(len(nums)):
            sol[i] = left[i] * right[i]

        return sol

            


            
        