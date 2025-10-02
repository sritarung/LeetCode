class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = numBottles
        total = numBottles
        while emptyBottles >= numExchange:
            total += 1
            emptyBottles -= numExchange
            emptyBottles += 1
            numExchange += 1
        return total


