class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        myDic = {}
        output = []

        for num in nums:
            myDic[num] = myDic.get(num, 0) + 1

        for key, value in myDic.items():
            freq[value].append(key)

        for i in range(len(nums), 0, -1):
            if freq[i] and k > 0:
                for num in freq[i]:
                    output.append(num)
                    k -= 1

        return output



        