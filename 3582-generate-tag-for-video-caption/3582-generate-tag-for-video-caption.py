class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.strip().split()

        if words == []:
            return "#"
            
        result = "#" + words[0].lower()
        for word in words[1:]:
            result += word[0].upper() + word[1:].lower()
        return result[:100]

        