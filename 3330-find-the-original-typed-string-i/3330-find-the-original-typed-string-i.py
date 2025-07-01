class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        prevChar = word[0]
        for w in word[1:]:
            if prevChar == w:
                ans += 1
            prevChar = w
        return ans
