class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        string_s = {}        
        for s_letter in s:
            if s_letter in string_s:
                string_s[s_letter] += 1
            else:
                string_s[s_letter] = 1
        
        string_t = {}        
        for t_letter in t:
            if t_letter in string_t:
                string_t[t_letter] += 1
            else:
                string_t[t_letter] = 1
        
        if string_s == string_t:
            return True
        else:
            return False
