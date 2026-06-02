class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prefix = [1] * n
        suffix = [1] * n

        i = 1
        while i < n:
            prefix[i] = prefix[i-1] * nums[i-1]
            i += 1

        i = n - 2
        while i >= 0:
            suffix[i] = suffix[i+1] * nums[i+1]
            i -= 1

        i = 0
        while i < n:
            result[i] = prefix[i] * suffix[i]
            i += 1

        return result


            
        