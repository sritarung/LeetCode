class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        increase = [0]* len(nums)
        count = 1
        if k == 1:
            return True
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                count += 1
            else:
                count = 1
            increase[i] = count
            if count >= k and i-k >= 0 and increase[i-k] >= k:
                return True
        return False

