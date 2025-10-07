from bisect import bisect_right
from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        
       
       # store list of index of dry days 
       # bisect_right to find the (index)day after the last flood, where u need to drain the river
       # need a lake dictionary to get the last time it was full
       # change ans[idx] to the value of this lake
        n = len(rains)
        last = {}
        dry_days = []
        ans = [-1] * n
        for i, r in enumerate(rains):
            if r > 0:
                if r in last:
                    j = bisect_right(dry_days, last[r])
                    if j == len(dry_days):
                        return []
                    
                    dry_day_idx = dry_days.pop(j)
                    ans[dry_day_idx] = r
                last[r] = i
                
            else:
                dry_days.append(i)
                ans[i] = 1
        return ans

    


