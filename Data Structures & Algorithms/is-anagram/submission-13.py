class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        string_s, string_t = {}, {}        
        both = len(s)

        for i in range(both):
            string_s[s[i]] = string_s.get(s[i], 0) + 1
            string_t[t[i]] = string_t.get(t[i], 0) + 1
        
        return string_s == string_t