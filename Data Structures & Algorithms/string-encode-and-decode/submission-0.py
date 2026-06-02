class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for wrd in strs:
            output +=   str(len(wrd))+ "#" + wrd
        return output


    def decode(self, s: str) -> List[str]:
        cnt = 0
        output = []
        while ( cnt < len(s)):
            tmpSize = ""
            tmpWrd = ""
            while(s[cnt] != "#"):
                tmpSize += s[cnt]
                cnt+=1
            cnt += 1
            for i in range(int(tmpSize)):
                tmpWrd += s[cnt]
                cnt += 1
            
            output.append(tmpWrd)
        return output
                        



