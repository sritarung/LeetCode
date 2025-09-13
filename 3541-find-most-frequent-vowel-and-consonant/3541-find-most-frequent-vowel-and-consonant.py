class Solution:
    def maxFreqSum(self, s: str) -> int:
        mp = {}
        max_freq_v = 0
        max_freq_c = 0
        for i in range(len(s)):
            if s[i] in mp:
                mp[s[i]] += 1
            else:
                mp[s[i]] = 1
        for i in range(len(s)):
            if s[i] in 'aeiou':
                max_freq_v = max(max_freq_v, mp[s[i]])
            else:
                max_freq_c = max(max_freq_c, mp[s[i]])
        
        return max_freq_v + max_freq_c