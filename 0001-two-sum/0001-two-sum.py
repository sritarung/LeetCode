class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force solution

        # iterate through the entire nums list in a double for loop
        # for each element, check if there is a complement element in the rest of the list
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
        # time complexity is O(n^2) 