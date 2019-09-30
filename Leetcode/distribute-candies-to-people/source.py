class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:

        ans = [0 for _ in range(num_people)]
        cnt = 1

        while candies - cnt >= 0:

            ans[(cnt-1)%num_people] += cnt
            candies -= cnt
            cnt += 1

        else:
            ans[(cnt-1)%num_people] += candies

        return ans
