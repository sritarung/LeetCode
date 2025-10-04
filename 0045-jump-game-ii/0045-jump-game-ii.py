class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def backtrack(i, steps):
            if i >= len(nums)-1:
                return 0
            if i in memo:
                return memo[i]

            minSteps = float('inf')
            
            for j in range(i+1, min(len(nums),i+nums[i]+1)):
                jumps_next = backtrack(j, steps+1)
                if jumps_next != float('inf'):
                    minSteps = min(minSteps, jumps_next + 1)
            memo[i] = minSteps
            return minSteps
        return backtrack(0,0)


