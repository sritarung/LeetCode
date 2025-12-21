from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = defaultdict(int)
        required = len(need)
        formed = 0
        min_len = float('inf')
        start = 0
        l = 0
        for r in range(len(s)):
            have[s[r]] += 1
            if s[r] in need and have[s[r]] == need[s[r]]:
                formed += 1
                
            while formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l

                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1
        return "" if min_len == float('inf') else s[start:start+min_len]