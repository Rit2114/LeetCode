class Solution:
    def maxSum(self, nums: List[int]) -> int:
        sum = 0
        st = set()
        mxNeg = float('-inf')
