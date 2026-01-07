class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen and left < right:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            ans = max(ans, right -left + 1)
        return ans
