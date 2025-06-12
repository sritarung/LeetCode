class Solution:
    def maxDifference(self, s: str) -> int:
        freq_mp = {}
        for i in range(len(s)):
            if s[i] not in freq_mp:
                freq_mp[s[i]] = 1
            else:
                freq_mp[s[i]] += 1
        
        max_odd = 0
        min_even = float('inf')
        for key, val in freq_mp.items():
            if val % 2 == 1:
                max_odd = max(val, max_odd)
            elif val > 0:
                min_even = min(min_even, val)
        
        return max_odd - min_even