class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ret = []

        count_nums = {} # value -> index
        for i, n in enumerate(nums):
            j = target - n # complement value 
            if j in count_nums: #check if its in there 
                return [nums.index(j), i]
            else:
                count_nums[n] = i #adding n (i) to the problem 
            
            
        return ret 