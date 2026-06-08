class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myDic = defaultdict(list)
        finDic = {}

        for i in range(len(nums)):
            myDic[nums[i]]

        myMax = 0 
        for num in nums:
            if num-1 not in myDic and num not in finDic:
                finDic[num] = finDic.get(num, 0) + 1
                curNum = num +1
                while(curNum in myDic):
                    finDic[num] = finDic.get(num, 0) + 1
                    curNum +=1

                if(myMax < finDic[num]):
                    myMax = finDic[num]


        return myMax




