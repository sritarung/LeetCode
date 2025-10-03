class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        leftHeight = height[left]
        rightHeight = height[right]
        res = 0
        while left < right:

            if height[left] < height[right]:
                leftHeight = max(leftHeight, height[left])
                res += leftHeight - height[left]
                left += 1
            else:
                rightHeight = max(rightHeight, height[right])
                res += rightHeight - height[right]
                right -= 1
        return res


