class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenSet = set()
        for c in brokenLetters:
            brokenSet.add(c)

        words = text.split(" ")
        output = len(words)
        for word in words:
            for c in word:
                if c in brokenSet:
                    output -= 1
                    break
        return output
                    
