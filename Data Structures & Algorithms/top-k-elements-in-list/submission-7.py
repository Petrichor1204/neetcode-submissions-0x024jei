class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use hash map to count frequency
        # use buckets with each index representing frequency
        #fill each slot and return till k
        slots = [[] for _ in range(len(nums)+ 1)]
        freq = {}
        res = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        # {1:1, 2:2, 3:3}
        for num in freq:
            val = freq[num]
            slots[val].append(num)
        count = 0
 
        for slot in reversed(slots):
            if count == k:
                break
            for num in slot:
                res.append(num)
                count += 1

            # O(n + m*n)
        
            
        return res
        
        


