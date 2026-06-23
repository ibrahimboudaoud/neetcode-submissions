class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDic = {}
        for i in range(len(nums)):
            myDic[nums[i]] = i
        for index, value in enumerate(nums):
            diff = target - value
            if diff in myDic and myDic[diff] != index:
                return [index, myDic[diff]]
        return []

        