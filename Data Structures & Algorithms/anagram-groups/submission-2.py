class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        myDic = defaultdict(list)
        for i in range(len(strs)):
            tmp = [0] * 26
            for n in range(len(strs[i])):
                pos = ord(strs[i][n]) - ord('a')
                tmp[pos] += 1
            myDic[tuple(tmp)].append(strs[i])

        for key, value in myDic.items():
            output.append(value)
        return output
        



        