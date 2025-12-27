class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        maxAvg = float('-inf')
        total = 0
        for right in range(len(nums)):
            total += nums[right]
            print(total)
            if right >= k-1:
                maxAvg = max(maxAvg, total/k)
                total -= nums[left]
                left += 1
        return maxAvg
            