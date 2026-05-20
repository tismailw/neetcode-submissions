class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        for i, val in enumerate(strs):
            
            key = ''.join(sorted(val))

            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(val)
        return list(anagrams.values())