class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtrack
        output = []
        curr = []
        def backtrack(index):
            output.append(curr[:])
            for i in range(index, len(nums)):
                curr.append(nums[i])
                backtrack(i+1)
                curr.pop()
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