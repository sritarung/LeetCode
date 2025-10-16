class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mp = defaultdict(lambda: 0)
        for n in nums:
            mp[n%value] += 1
        
        mex = 0
        while mp[mex % value] > 0:
            mp[mex % value] -= 1
            mex += 1
        return mex