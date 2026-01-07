class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        left = 0
        ans = 0
        max_freq = 0
        for right in range(len(s)):
            counter[s[right]] += 1
            max_freq = max(max_freq,counter[s[right]])
            window = right - left + 1
            if k + max_freq >= window:
                ans = max(ans, window)
            else:
                counter[s[left]] -= 1
                left += 1
        return ans
