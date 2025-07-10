class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        count = len(startTime)
        prefixSum = [0] * (count + 1)
        maxFree = 0

        for i in range(count):
            prefixSum[i + 1] = prefixSum[i] + (endTime[i] - startTime[i])
        
        for i in range(k, count + 1):
            occupied = prefixSum[i] - prefixSum[i - k]
            windowStart = 0 if i == k else endTime[i-k-1]
            windowEnd = eventTime if i == count else startTime[i]
            totalWindowTime = windowEnd - windowStart
            free = totalWindowTime - occupied
            maxFree = max(maxFree, free)
        
        return maxFree