class Solution:
    def isValid(self, s: str) -> bool:
        myDic = {'(':')', '[':']','{':'}'}
        stack = deque()

        for let in s:
            if(let in myDic):
                stack.append(let)

            else:
                if(not stack):
                    return False
                if(myDic[stack[-1]] != let):
                    return False
                stack.pop()
        
        return not stack

            
        


        