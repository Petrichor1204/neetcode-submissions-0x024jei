class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # given an array return the top k most freq elements
        # nums = [1,2,2,3,3,3], k = 2
        freq = {}
        result = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        freq = sorted(freq.items(), key = lambda x: x[1], reverse=True)
        
        count = 0
        for key, value in freq:
            result.append(key)
            count += 1
            if count == k:
                return result



        