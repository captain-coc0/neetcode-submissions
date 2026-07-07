class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqDict = {}
        for string in strs:
            alphaFreq = [0]*26
            for char in string:
                alphaFreq[ord(char)-ord('a')] += 1
            
            freqTuple = tuple(alphaFreq)
            if freqTuple in freqDict:
                freqDict[freqTuple].append(string)
            else:
                freqDict[freqTuple] = [string]

        return list(freqDict.values())
                