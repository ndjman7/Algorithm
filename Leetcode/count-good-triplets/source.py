class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        answer = 0
        length = len(arr)
        li = list()
        def find_good_triplet(count, index):

            if count == 3:
                if (
                    abs(li[0] - li[1]) <= a and
                    abs(li[1] - li[2]) <= b and
                    abs(li[0] - li[2]) <= c
                ):
                    nonlocal answer
                    answer += 1
                return

            for i, element in enumerate(arr[index:]):
                next_index = i + 1 + index
                if next_index > length:
                    continue
                li.append(element)
                find_good_triplet(count + 1, next_index)
                li.pop()


        find_good_triplet(0, 0)
        return answer

