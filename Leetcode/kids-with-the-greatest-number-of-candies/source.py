class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = 0
        answer = []
        for candy in candies:
            max_candies = max(candy, max_candies)

        for candy in candies:
            if candy + extraCandies >= max_candies:
                answer.append(True)
            else:
                answer.append(False)

        return answer

