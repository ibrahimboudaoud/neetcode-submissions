class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myMap = defaultdict(int)
        myMap2 = defaultdict(int)


        for char in s:
            myMap[char] += 1
        
        for char in t:
            myMap2[char] += 1

        return myMap == myMap2

        