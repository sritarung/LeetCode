from bisect import bisect_right
from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n              # -1 on rain days; on dry days we'll set which lake to dry
        last = {}                   # lake -> last day it rained (lake is full since that day)
        dry_days = []               # sorted list of indices of days where rains[i] == 0

        for i, lake in enumerate(rains):
            if lake > 0:
                # It's raining on `lake`
                if lake in last:
                    # We must dry `lake` on some dry day after last[lake] and before today (i)
                    j = bisect_right(dry_days, last[lake])  # first dry day index > last[lake]
                    if j == len(dry_days):
                        return []  # no available dry day to prevent flood
                    dry_day_idx = dry_days.pop(j)           # use that dry day
                    ans[dry_day_idx] = lake                 # dry this specific lake on that day
                # Mark that lake just got filled today
                last[lake] = i
                ans[i] = -1
            else:
                # It's a dry day; record its index for later assignment
                dry_days.append(i)
                ans[i] = 1  # placeholder; if unused, drying any lake (1) is fine

        return ans
