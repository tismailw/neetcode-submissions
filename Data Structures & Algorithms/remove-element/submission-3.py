class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        write = 0

        #if val is not in nums then we print out k = 0 
        
        if val not in nums:
            return len(nums) 
    

        #if val is in nums

        for read in range(0, len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        return write 