class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sMap = {}
        for i in s:
            if i in sMap:
                sMap[i] += 1
            else:
                sMap[i] = 1
        
        tMap = {}
        for i in t:
            if i in tMap:
                tMap[i] += 1
            else:
                tMap[i] = 1

        if sMap == tMap:
            return True
        else:
            return False
        
