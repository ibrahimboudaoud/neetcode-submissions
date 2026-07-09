class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        tmp = [] 
        cnt = 0
        while(cnt < len(s)):
            cur = s[cnt]
            wrdLen = 0
            myLen = ""
            tmpWord = ""
            while(cur != "#"):
                myLen += cur
                cnt += 1
                cur = s[cnt]
                wrdLen = int(myLen)
            cnt += 1
            for i in range(wrdLen):
                tmpWord += s[cnt]
                cnt += 1

            tmp.append(tmpWord)

        return tmp

        
