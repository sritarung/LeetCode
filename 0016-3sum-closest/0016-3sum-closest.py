class Solution:
    def bisectRight(self, nums, target, idx):
        lo = idx
        hi = len(nums)
        while lo < hi:
            mid = lo + (hi - lo)//2
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid
        return lo
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                complement = target - nums[i] - nums[j]
                hi = bisect_right(nums, complement, j+1)
                lo = hi -1
                if hi < len(nums) and abs(diff) > abs(complement - nums[hi]):
                    diff = complement - nums[hi]
                if lo > j and abs(diff) > abs(complement - nums[lo]):
                    diff = complement - nums[lo]
            if diff == 0:
                break
        return target - diff
