class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "@" + s
        return encodedStr

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                num = ""
                while s[i] != "@":
                    num+= s[i]
                    i += 1
                #at @
                length = int(num)
                #first letter
                tempStr = ""
                for j in range(length):
                    i += 1
                    tempStr += s[i]
                #now beginning of next number
                strs.append(tempStr)
                i += 1
        return strs
