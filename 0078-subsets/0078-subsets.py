class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtrack
        output = []
        curr = []
        def backtrack(index):
            if index == len(nums):
                output.append(curr[:])
                return
            curr.append(nums[index])
            backtrack(index+1)
            curr.pop()
            backtrack(index+1)
        backtrack(0)
        return output


        # cascading
        # output = [[]]
        # for num in nums:
        #     newSubsets = []
        #     for curr in output:
        #         temp = curr.copy()
        #         temp.append(num)
        #         newSubsets.append(temp)
        #     for curr in newSubsets:
        #         output.append(curr)
        # return output