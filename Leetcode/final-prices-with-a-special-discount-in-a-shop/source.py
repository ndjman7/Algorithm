class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        for index, price in enumerate(prices):
            for next_price in prices[index+1:]:
                if price >= next_price:
                    answer.append(price - next_price)
                    break
            else:
                answer.append(price)

        return answer
