class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        theT, theS = {}, {}
        
        for i in range(len(s)):
            theT[t[i]] = 1 + theT.get(t[i], 0)
            theS[s[i]] = 1 + theS.get(s[i],0)

        return theT == theS


        