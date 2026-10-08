from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # goal: return the k most frequent elements within the arr
        # using bucket sort where there is a list at each index
        # elements with that count go into the list
        # we loop in reverse to get top k
        result = []
        bucket = [[] for _ in range(len(nums) + 1)]

        counts = Counter(nums)

        for num, count in counts.items():
            bucket[count].append(num)

        # [[][1][2][3]]
        c = 0
        for b in reversed(bucket):
            for num in b:
                if c == k:
                    break
                result.append(num)
                c += 1
                
        return result


