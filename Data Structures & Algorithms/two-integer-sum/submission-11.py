class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDic = {}

        for i in range(len(nums)):
            myDic[nums[i]] = i

        for i in range(len(nums)):
            if(target - nums[i] in myDic and myDic[target - nums[i]] != i):
                return [i, myDic[target - nums[i]]]
        
        return []

        
        