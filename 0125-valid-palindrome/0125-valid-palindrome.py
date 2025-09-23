class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s) - 1
        l = 0
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True