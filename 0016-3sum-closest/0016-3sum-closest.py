class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        closest_sum = float('inf')
        nums.sort()
        for i in range(n-2):
            l = i + 1
            r = n - 1
            while l < r:
                total_num = nums[i] + nums[l] + nums[r]
                if abs(target - total_num) < abs(target - closest_sum):
                    closest_sum = total_num
                
                if total_num > target:
                    r -= 1
                else:
                    l += 1
        return closest_sum
