class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        total = 0
        seen = set()

        for right in range(len(nums)):
            curr= nums[right]
            if curr in seen:
                while curr in seen:
                    left_char = nums[left]
                    seen.remove(left_char)
                    total -= nums[left]
                    left += 1
            seen.add(curr)
            total += curr
            if len(seen) == k:
                ans = max(ans, total)
                seen.remove(nums[left])
                total -= nums[left]
                left += 1
        return ans
            
