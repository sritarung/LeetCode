from bisect import bisect_right
from typing import List

class Solution:
    def bisectRight(self, arr, target):
        # returns first index i where arr[i] > target
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            if mid < len(arr) and arr[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return l

    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        last = {}        # lake -> last index it rained (lake is full since then)
        dry_days = []    # sorted list of indices i where rains[i] == 0
        ans = [-1] * n

        for i, r in enumerate(rains):
            if r > 0:
                if r in last:
                    # need earliest dry day strictly after last[r]
                    j = self.bisectRight(dry_days, last[r])
                    if j == len(dry_days):
                        return []  # no dry day after last fill -> flood
                    dry_day_idx = dry_days.pop(j)
                    ans[dry_day_idx] = r  # dry lake r on that dry day
                last[r] = i
                # ans[i] already -1
            else:
                dry_days.append(i)  # indices naturally stay sorted as i increases
                ans[i] = 1          # default; overwritten if we assign a specific lake

        return ans

    


