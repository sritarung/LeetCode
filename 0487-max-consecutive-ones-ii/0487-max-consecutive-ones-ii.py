class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        max_ones = 1
        count = 1
        for r in range(len(nums)):
            if nums[r] == 1:
                max_ones = max(max_ones, r - l + 1)
                continue
            if count > 0:
                count -= 1
                max_ones = max(max_ones, r - l + 1)
                continue
            while count == 0:
                if nums[l] == 0:
                    count += 1
                l += 1
            count -= 1
        return max_ones