class Solution:
    def doesAliceWin(self, s: str) -> bool:
        num_of_vowels= 0
        for i in range(len(s)):
            if s[i] in "aeiou":
                num_of_vowels += 1
        return True if num_of_vowels != 0 else False