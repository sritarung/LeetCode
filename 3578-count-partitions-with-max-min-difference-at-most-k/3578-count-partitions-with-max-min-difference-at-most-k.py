class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        dp = [0] * (n+1)
        dp[0] = 1

        left = 0
        minDeque = deque()
        maxDeque = deque()
        prefixSum = [0] * (n+1)
        prefixSum[0] = 1

        for right in range(1, n+1):
            num = nums[right-1]
            while minDeque and nums[minDeque[-1]] >= num:
                minDeque.pop()
            minDeque.append(right-1)

            while maxDeque and nums[maxDeque[-1]] <= num:
                maxDeque.pop()
            maxDeque.append(right-1)

            while nums[maxDeque[0]] - nums[minDeque[0]] > k:
                left += 1
                if minDeque[0] < left:
                    minDeque.popleft()
                if maxDeque[0] < left:
                    maxDeque.popleft()

            dp[right] = (prefixSum[right - 1] - prefixSum[left - 1] if left > 0 else prefixSum[right - 1]) % MOD
            prefixSum[right] = (prefixSum[right - 1] + dp[right]) % MOD

        return dp[n] 
