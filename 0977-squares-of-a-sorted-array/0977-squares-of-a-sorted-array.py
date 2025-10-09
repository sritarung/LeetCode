class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        l = 0
        r = len(nums)-1
        pos = len(nums)-1
        while l <= r:
            if nums[r] > abs(nums[l]):
                ans[pos] = nums[r] * nums[r]
                r -= 1
            else:
                ans[pos] = nums[l] * nums[l]
                l += 1
            pos -= 1
        return ans


            