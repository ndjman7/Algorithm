class OrderedStream:

    def __init__(self, n: int):
        self._n = n
        self._pointer = 0
        self._list = [None for _ in range(n)]


    def insert(self, id: int, value: str) -> List[str]:
        index = id-1
        self._list[index] = value
        if index == self._pointer:
            next_index = index + 1
            while next_index < self._n:
                if self._list[next_index] is None:
                    break

                next_index += 1
            self._pointer = next_index
            return self._list[index:next_index]

        return []
