class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        ans = 0
        counter = 0
        for right in range(len(s)):
            if s[right] in 'aeiou':
                counter += 1
            if right - left + 1 == k:
                ans = max(ans, counter)
                if s[left] in 'aeiou':
                    counter -= 1
                left += 1
        return ans
