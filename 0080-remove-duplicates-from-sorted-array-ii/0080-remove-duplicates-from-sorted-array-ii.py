class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 0
        mp = defaultdict(lambda: 0)
        for i in range(len(nums)):
            if mp[nums[i]] != 2:
                mp[nums[i]] += 1
                nums[prev] = nums[i]
                prev += 1
        return prev
                



