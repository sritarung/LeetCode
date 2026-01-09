class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(nums, k):
            l, r, cnt = 0, 0, 0
            mp = defaultdict(int)
            while r < len(nums):
                mp[nums[r]] += 1
                while len(mp) > k:
                    mp[nums[l]] -= 1
                    if mp[nums[l]] == 0:
                        del mp[nums[l]]
                    l += 1
                
                cnt += r - l + 1
                r += 1
            return cnt
        return helper(nums, k) - helper(nums, k-1)
