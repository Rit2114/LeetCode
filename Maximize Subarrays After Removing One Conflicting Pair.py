class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        right = [[] for _ in range(N + 1)]
        for a, b in A:
            right[max(a, b)].append(min(a, b))

        ans = 0
        left = [0, 0]
        imp = [0] * (N + 1)
        
