class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r-l)//2
            if mid < r and nums[mid] < nums[mid + 1]:
                l= mid + 1
            else:
                r = mid
        return l