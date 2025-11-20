class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = (10 ** 9) + 7
        unique=6
        repeating=6
        for i in range(2,n+1):
            temp=unique
            unique=3*unique+2*repeating
            repeating=2*temp+2*repeating
        return (unique+repeating)%MOD
