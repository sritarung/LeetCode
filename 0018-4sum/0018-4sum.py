class Solution:
    def twoSum(self, nums, target, start):
        results = []  # FIX 1: Create a list to hold ALL pairs
        left = start
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                # FIX 2: Found a match! Add VALUES, not indices.
                results.append([nums[left], nums[right]])
                
                # FIX 3: Skip duplicates internally to avoid repeating pairs
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                    
        return results
    
    def nSum(self, nums, target, start, n):
        results = []
        if n== 2:
            return self.twoSum(nums, target, start)
        for i in range(start, len(nums)-n + 1):
            if i > start and nums[i] == nums[i-1]:
                continue
            current_num = nums[i]

            sub_result = self.nSum(nums, target - current_num, i + 1, n - 1)
            for sub_list in sub_result:
                results.append([current_num] + sub_list)
        return results

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.nSum(nums, target, 0, 4)