class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sort_deck = sorted(deck)
        n = len(sort_deck)

        if n == 0: return []
        if n == 1: return sort_deck
        result = [sort_deck[n-2], sort_deck[n-1]]
        if n == 2: return result

        for i in range(n-3, -1, -1):
            last = result.pop()
            result.insert(0, last)
            result.insert(0, sort_deck[i])

        return result
