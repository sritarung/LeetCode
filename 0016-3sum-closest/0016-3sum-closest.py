class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo = i + 1
            hi = len(nums)-1
            while lo < hi:
                total = nums[lo] + nums[hi] + nums[i]
                if abs(target - total) < abs(diff):
                    diff = target - total
                if total < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff

