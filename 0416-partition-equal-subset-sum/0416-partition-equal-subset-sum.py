class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)% 2:
            return False
        target = sum(nums)//2
        dp = set()
        dp.add(0)
        for i in range(len(nums) -1, -1, -1):
            temp = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                temp.add(t + nums[i])
                temp.add(t)
            dp = temp
        return False
