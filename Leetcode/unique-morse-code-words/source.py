class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans_list = []
        ret = 0
        for word in words:
            ans = ''
            for char in word:
                idx = ord(char) - ord('a')
                ans += morse[idx]
            if ans not in ans_list:
                ans_list.append(ans)
                ret += 1
        return ret
