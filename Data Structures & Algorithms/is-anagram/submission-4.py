class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        for letter in s:
            sMap[letter] = sMap.get(letter, 0) + 1
        for letter in t:
            tMap[letter] = tMap.get(letter, 0) + 1

        for key in sMap:
            if len(sMap) != len(tMap):
                return False
            if key not in tMap:
                return False
            elif sMap[key] != tMap[key]:
                return False
        
        return True