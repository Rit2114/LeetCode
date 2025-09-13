class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq=Counter(s)
        maxCV=[0]*2
        for i, f in freq.items():
