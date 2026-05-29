class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        everything = {}
        for str in strs: 

            sorted_str = sorted(str)
            clean_str = "".join(sorted_str)

            if (clean_str not in everything):
                everything[clean_str] = []
                everything[clean_str].append(str)
            else:
                everything[clean_str].append(str)

        return list(everything.values())
