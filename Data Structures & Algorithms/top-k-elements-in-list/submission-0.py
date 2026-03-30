class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for n in nums:
            res[n] += 1
        freq = [x[0] for x in sorted(res.items(), key = lambda x: x[1], reverse = True)[:k]]
        return freq