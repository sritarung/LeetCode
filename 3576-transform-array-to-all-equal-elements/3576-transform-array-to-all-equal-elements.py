class Solution:
    def solve(self,nums, target):
        cnt = 0
        for i in range(len(nums)-1):
            if nums[i] != target:
                cnt += 1
                nums[i] = -nums[i]
                nums[i+1] = -nums[i+1]
        return cnt if nums[-1] == target else float('inf')

    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        return self.solve(nums[:],1) <= k or self.solve(nums[:],-1) <= k


    
    
