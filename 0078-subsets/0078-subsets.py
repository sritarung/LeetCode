class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # cascading
        output = [[]]
        for num in nums:
            newSubsets = []
            for curr in output:
                temp = curr.copy()
                temp.append(num)
                newSubsets.append(temp)
            for curr in newSubsets:
                output.append(curr)
        return output