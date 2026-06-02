class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHM = {}
        myL = []
        for index, item in enumerate(nums):
            if target - item in myHM:
                myL.append(myHM.get(target - item))
                myL.append(index)
                return myL
            else:
                myHM[item] = index
        return myL
        
        

         



        