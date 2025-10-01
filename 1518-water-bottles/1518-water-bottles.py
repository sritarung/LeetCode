class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles  # all initial bottles get drunk
        empty = numBottles  # now they’re empty
        
        while empty >= numExchange:
            # exchange empties for new bottles
            new_bottles = empty // numExchange
            total += new_bottles  # drink them
            # update empties = leftover empties + new empties
            empty = empty % numExchange + new_bottles
        
        return total
