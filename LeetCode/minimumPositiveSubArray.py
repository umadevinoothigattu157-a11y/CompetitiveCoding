class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        mini = float('inf')
        n = len(nums)

        for i in range(n):
            total = 0

            for j in range(i, n):
                total += nums[j]
                length = j - i + 1

                if l <= length <= r and total > 0:
                    mini = min(mini, total)

        if mini == float('inf'):
            return -1

        return mini
