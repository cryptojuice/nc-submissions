import functools
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        results = []
        for num in counts:
            buckets[counts[num]].append(num)
        
        for n in range(len(buckets) - 1, -1, -1):
            for j in buckets[n]:
                if len(results) == k:
                    break
                results.append(j)
            if len(results) == k:
                break
        return results
        