class Solution:
    symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    
    def romanToInt(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-1):
            if self.symbols[s[i]] < self.symbols[s[i+1]]:
                ans -= self.symbols[s[i]]
            else:
                ans += self.symbols[s[i]]
            
        ans += self.symbols[s[-1]]
        return ans
