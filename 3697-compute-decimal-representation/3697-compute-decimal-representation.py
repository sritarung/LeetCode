class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        result = []
        i = 0
        while n:
            d = n % 10
            if d:
                result.append(d*10**i)
            i += 1
            n //= 10
        return result[::-1]



