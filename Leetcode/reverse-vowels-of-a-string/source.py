class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s) - 1
        vowels = ['i', 'e', 'a', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ret = list(s)
        while i < j:
            if s[i] in vowels and s[j] in vowels:
                temp = ret[i]
                ret[i] = ret[j]
                ret[j] = temp
                i += 1
                j -= 1
            elif ret[i] in vowels:
                j -= 1
            elif ret[j] in vowels:
                i += 1
            else:
                i += 1
                j -= 1
        return "".join(ret)
