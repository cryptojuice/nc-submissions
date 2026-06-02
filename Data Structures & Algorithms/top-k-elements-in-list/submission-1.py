import functools

class Solution:
    def compareItems(self, item1, item2):
        if item1['value'] > item2['value']:
            return -1
        elif item1['value'] < item2['value']:
            return 1
        else:
            return 0
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        seen_array = []
        ans = []
        for n in nums:
            if n not in seen:
                seen[n] = 1
            else:
                seen[n] = seen[n] + 1

        for key in seen.keys():
            seen_array.append({'key': key, 'value': seen[key]})

        sorted_seen = sorted(seen_array, key=functools.cmp_to_key(self.compareItems))
        print(sorted_seen)
        
        for i in range(k):
            ans.append(sorted_seen[i]['key'])

        return ans
        