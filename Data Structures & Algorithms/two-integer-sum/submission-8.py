class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        potential = {}

        for i, val in enumerate(nums):

            other = target - val

            if other in potential:
                prev = potential[other]

                return [prev, i]                
            else:
                potential[val] = i