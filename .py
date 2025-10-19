class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        
        l = len(s)
        q = deque([s])
        seen = set([s])
        res = s
