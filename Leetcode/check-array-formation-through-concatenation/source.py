class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:

        piece_length = len(pieces)
        piece_count = 0
        def _check(arr, piece):
            nonlocal piece_count
            piece_count += 1
            if len(arr) < len(piece):
                return False
            for a, b in zip(arr, piece):
                if a != b:
                    return False
            return True

        for piece in pieces:
            for idx, el in enumerate(arr):
                if el != piece[0]:
                    continue
                if not _check(arr[idx:], piece):
                    return False
        if piece_length != piece_count:
            return False

        return True

