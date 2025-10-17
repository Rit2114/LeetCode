class Solution(object):
    def maxPartitionsAfterOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == self.ALPHABET_SIZE:
            return 1

        n = len(s)
        ansr = [0] * n
        usedr = [0] * n
        used = 0
        cntUsed = 0
        ans = 1
