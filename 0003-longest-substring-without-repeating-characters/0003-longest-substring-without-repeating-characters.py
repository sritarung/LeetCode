class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        seen = set()
        max_len = 0
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            if r - l + 1 > max_len:
                max_len = r - l + 1
            seen.add(s[r])
            r += 1
        return max_len

