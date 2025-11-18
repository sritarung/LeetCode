
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
                    
        return results # Return list of lists
            
    def kSumHelper(self, nums, target, start, k):
        results = []
        
        # Base Case
        if k == 2:
            return self.twoSum(nums, target, start)
        
        # Recursive Step
        for i in range(start, len(nums) - k + 1):
            # Skip duplicates for the current position
            if i > start and nums[i-1] == nums[i]:
                continue
            
            current_num = nums[i]

            # Recursively find (k-1) sum
            sub_result = self.kSumHelper(nums, target - current_num, i + 1, k - 1)

            # Combine current number with the results from recursion
            for sub_list in sub_result:
                results.append([current_num] + sub_list)
                
        return results

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # k=3, target=0
        return self.kSumHelper(nums, 0, 0, 3)
       