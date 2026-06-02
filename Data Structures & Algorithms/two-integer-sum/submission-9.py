class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDic = {}
        for index, value in enumerate(nums):
            diff = target - value
            if( diff in myDic):
                return [myDic[diff], index]
            myDic[value] = index


    
        

        