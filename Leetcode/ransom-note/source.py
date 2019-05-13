class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine = list(magazine)
        for note in ransomNote:
            exist = False
            for m in magazine:
                if note == m:
                    magazine.remove(m)
                    exist = True
                    break
            if exist == False:
                return False
        return True
