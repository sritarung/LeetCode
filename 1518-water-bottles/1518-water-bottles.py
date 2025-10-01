class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = 0
        while numBottles >= numExchange:
            numBottles //= numExchange
            empty = numBottles % numExchange
            total += numBottles
            numBottles += empty
        return total