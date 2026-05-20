class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1

#       [2,7,11,15], target = 9
        while(left < right):
            if(numbers[left] + numbers[right] == target): 
                break
            if(numbers[left] + numbers[right] > target):
                right = right - 1
            if(numbers[left] + numbers[right] < target):
                left = left + 1
        return [left+1,right+1]
