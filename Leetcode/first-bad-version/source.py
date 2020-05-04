# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def find_bad_version(l, r):
            if l == r:
                return l
            m = int((l+r) / 2)
            if isBadVersion(m):
                return find_bad_version(l, m)
            else:
                return find_bad_version(m+1, r)
        
        return find_bad_version(1, n)

