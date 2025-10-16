class Solution:
    def bisect_left(self, nums, target, i):
        nums = nums[i:]
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = lo + (hi - lo)//2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                complement = target - nums[i] - nums[j]
                left = bisect_left(nums, complement, j+1)
                ans += left - j-1
        return ans 
                