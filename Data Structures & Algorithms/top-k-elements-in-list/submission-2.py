class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = [[] for i in range(len(nums)+1)]

        myDic = {}

        for num in nums:
            myDic[num] = myDic.get(num, 0) + 1

        for num, freq in myDic.items():
            output[freq].append(num)

        tmpLen = len(output) -1
        res = []
        
        while (k >0 and tmpLen > 0 ):
            if(len(output[tmpLen]) > 0 ):
                for tmp in output[tmpLen]:
                    res.append(tmp)
                    k-=1
            tmpLen -=1
        return res


    


            
        