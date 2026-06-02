class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        myDic = {}
        for i in range(len(strs)):
            tmpKey = [0] * 26 
            for n in range(len(strs[i])):
                tmpKey[ord((strs[i])[n]) - ord('a')] += 1
            myDic.setdefault(tuple(tmpKey), []).append(strs[i])
        
        output.extend(list(myDic.values()))
        
        return output

        
        