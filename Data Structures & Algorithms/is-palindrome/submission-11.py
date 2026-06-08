class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = 0
        tmp = ""
        for letter in s:
            if letter.isalpha() or letter.isalnum():
                tmp += letter

        upper = len(tmp)-1



        while(lower <= upper ):
            if(tmp[upper].lower() != tmp[lower].lower()):
                return False
            lower +=1
            upper -= 1
        
        return True

        