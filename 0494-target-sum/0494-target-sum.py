class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def recursion(index, total):
            if index == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (index, total) in dp:
                return dp[(index, total)]
            
            res = 0
            res += recursion(index + 1, total + nums[index])
            res += recursion(index + 1, total - nums[index])

            dp[(index, total)] = res
            return res
        return recursion(0, 0)




