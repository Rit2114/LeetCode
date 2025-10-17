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

        for i in range(n - 1, -1, -1):
            ch = ord(s[i]) - ord('a')
            if (used & (1 << ch)) == 0:
                if cntUsed == k:
                    cntUsed = 0
                    used = 0
                    ans += 1
                used |= (1 << ch)
                cntUsed += 1
            ansr[i] = ans
            usedr[i] = used

            l = 0
        while l < n:
            used = 0
            cntUsed = 0
            usedBeforeLast = 0
            usedTwiceBeforeLast = 0
            last = -1
            r = l

            while r < n:
                ch = ord(s[r]) - ord('a')
                if (used & (1 << ch)) == 0:
                    if cntUsed == k:
                        break
                    usedBeforeLast = used
                    last = r
                    used |= (1 << ch)
                    cntUsed += 1
                elif cntUsed < k:
                    usedTwiceBeforeLast |= (1 << ch)
                r += 1

        ansl = 0
        ans = ansr[0]
