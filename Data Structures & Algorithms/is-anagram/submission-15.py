class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count_s = {}

        for i in s: 
            if i not in count_s:
                count_s[i] = 1
            else:
                count_s[i] += 1

        count_t = {}

        for i in t: 
            if i not in count_t:
                count_t[i] = 1
            else:
                count_t[i] += 1

        if count_s == count_t:
            return True
        return False

