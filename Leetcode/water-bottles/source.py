class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        answer = numBottles
        rest = numBottles % numExchange
        numBottles = numBottles // numExchange
        while numBottles > 0:
            answer += numBottles
            new_rest = (numBottles + rest) % numExchange
            numBottles = (numBottles + rest) // numExchange
            rest = new_rest
        return answer

