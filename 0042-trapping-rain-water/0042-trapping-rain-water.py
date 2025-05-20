class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = height[0]
        rightMax = height[len(height)-1]
        left = 0
        right = len(height)-1
        res = 0
        while left <= right:
            if leftMax < rightMax:
                leftMax = max(height[left], leftMax)
                res += leftMax - height[left]
                left += 1
            else:
                rightMax = max(height[right], rightMax)
                res += rightMax - height[right]
                right -= 1
        return res