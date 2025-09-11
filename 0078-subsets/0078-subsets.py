class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # lexicographic subsets ( binary sorted subsets)
        n = len(nums)
        output = []
        for i in range(2 ** n, 2 ** (n + 1)):
            bitmask = bin(i)[3:]

            output.append([nums[j] for j in range(n) if bitmask[j] == "1"])

        return output
        
        # backtrack
        # output = []
        # curr = []
        # def backtrack(index):
        #     if index == len(nums):
        #         output.append(curr[:])
        #         return
        #     curr.append(nums[index])
        #     backtrack(index+1)
        #     curr.pop()
        #     backtrack(index+1)
        # backtrack(0)
        # return output


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