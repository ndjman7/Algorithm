class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combination_length = combinationLength
        self.length = len(characters)
        self.lexi_order = []
        self.lexi_index = 0
        self._set_lexi_order(0, [])


    def _set_lexi_order(self, index, new_order):

        if len(new_order) == self.combination_length:
            self.lexi_order.append(new_order[:])
            return

        for i in range(index, self.length):
            new_order.append(self.characters[i])
            self._set_lexi_order(i+1, new_order)
            new_order.pop()

    def next(self) -> str:
        next_order = self.lexi_order[self.lexi_index]
        self.lexi_index += 1
        return "".join(next_order)

    def hasNext(self) -> bool:
        if len(self.lexi_order) <= self.lexi_index:
            return False
        return True
