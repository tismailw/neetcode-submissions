class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        tracker = {}

        for i, val in enumerate(nums):
            key = target - val
            if key in tracker: 
                print(i)
                print(tracker[key])
                return [tracker[key], i]
            else:
                tracker[val] = i
