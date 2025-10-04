class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxAmount = 0
        while l < r:
            amount = min(height[l], height[r]) * (r - l)
            maxAmount = max(amount, maxAmount)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxAmount
