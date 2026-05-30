class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = []
        for i in range(len(nums) + 1):
            freq.append([])

        for n in nums:
            count[n] = 1 + count.get(n, 0) #hashmap
            
        for num, cnt in count.items():
            freq[cnt].append(num)

        result = []

        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return 

