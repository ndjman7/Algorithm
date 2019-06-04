class Solution:
    def rotatedDigits(self, N: int) -> int:
        required_numbers = ['2', '5', '6', '9']
        bad_numbers = ['3', '4', '7']
        ans = 0
        for num in range(1, N+1):
            required = False
            for c in str(num):
                if c in bad_numbers:
                    required = False
                    break
                if c in required_numbers:
                    required = True
            if required:
                ans += 1
                required = False
        return ans
