class Solution:
    def isPalindrome(self, s: str) -> bool:
        up = len(s) - 1
        low = 0
        while(low <= up): 
            if not s[low].isalnum():
                low +=1
            if not s[up].isalnum():
                up -=1
            if low <= up and s[low].isalnum() and s[up].isalnum():
                if s[low].lower() != s[up].lower():
                    return False
                else:
                    low +=1
                    up -= 1
        return True


        