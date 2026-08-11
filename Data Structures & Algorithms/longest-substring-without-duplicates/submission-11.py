class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lets = set()
        longest = 0
        l = 0

        for r in range(len(s)):
            if s[r] in lets:
                while(s[r] in lets):
                    lets.remove(s[l])
                    l+= 1
            lets.add(s[r])
            longest = max(longest, r-l + 1)


        return longest


        