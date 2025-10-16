class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        r = 0
        l = 0
        product = 1
        ans = 0
        while r < len(nums):
            product *= nums[r]
            while product >= k and l <=r:
                product /= nums[l]
                l += 1

            ans += r - l + 1
            r += 1
        return ans
            