class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        reverse(nums,0,n-k-1)
        reverse(nums,n-k,n-1)
        reverse(nums,0,n-1)
def reverse(arr,start,end):
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -=1
