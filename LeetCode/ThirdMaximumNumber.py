class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        s = set(nums)
        li = sorted(s,reverse=True)
        if len(li)>=3:
            return li[2]
        else:
            return li[0]
