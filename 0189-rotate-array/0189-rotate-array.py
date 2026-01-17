class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        if n == 0:
            return
        k %= n
        nums[:] = nums[n-k:] + nums[:n-k]
