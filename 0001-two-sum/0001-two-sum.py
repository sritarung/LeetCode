class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two pass hashmap solution

        # use hashmap to store index values for each element in nums
        # if you find complement in hashmap and the value of it in hashmap is not current index, then u got the pair
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement]!= i:
                return [i, hashmap[complement]]
            
        return []

        # # brute force solution

        # # iterate through the entire nums list in a double for loop
        # # for each element, check if there is a complement element in the rest of the list
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []
        # # time complexity is O(n^2) 
