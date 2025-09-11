class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        charToNextIndex = {}
        ans = 0
        i = 0
        for j in range(n):
            if s[j] in charToNextIndex:
                i = max(charToNextIndex[s[j]], i)
            
            ans = max(ans, j - i + 1)
            charToNextIndex[s[j]] = j + 1
        return ans