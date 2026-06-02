class Solution:
    def isValid(self, s: str) -> bool:
        dictP = {"(" : ")", "[" : "]", "{" : "}"}
        myStack = []
        for c in s:
            if c in dictP:
                myStack.append(c)
            else:
                if len(myStack) != 0:
                    if dictP[myStack[-1]] != c:
                        return False
                    else:
                        myStack.pop()
                else:
                    return False
        return len(myStack) == 0
            


        