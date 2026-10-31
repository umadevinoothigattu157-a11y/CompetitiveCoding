class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        d = {0: 1}

        for i in nums:
            total += i

            if total - k in d:
                count += d[total - k]

            d[total] = d.get(total, 0) + 1

        return count
