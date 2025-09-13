class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # since we are returning the elements and not indicides, we can use sorting
        # sort nums
        # nums = [-1,0,1,2,-1,-4]
        nums.sort()
        # nums = [-4, -1, -1, 0, 1, 2]
        
        
        # nums = [-4, -4,-4, 0, 0, 1, 3, 4, 4]
        # Notice that the solution set must not contain duplicate triplets
        # -4 - 4 + 4 = -4
        # -4 + 0 + 4 = 0
        #[-1,-1,-1,0,2]
        output = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum_numbers = nums[i] + nums[l] + nums[r]
                if sum_numbers == 0:
                    output.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l]==nums[l+1]:
                        l += 1
                    l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                elif sum_numbers < 0:
                    while l < r and nums[l]==nums[l+1]:
                        l += 1
                    l += 1
                else:
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
        return output