class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myD1 = defaultdict(list)
        myD2 = defaultdict(list)
        if len(s) != len(t):
            return False
        for c1, c2 in zip(s, t):
            myD1[c1].append(c1)
            myD2[c2].append(c2)

        return myD1 == myD2




        