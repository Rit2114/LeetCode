class Solution:
    def maxSum(self, nums: List[int]) -> int:
        sum = 0
        st = set()
        mxNeg = float('-inf')
        for i in range(len(nums)):
            if nums[i] > 0:
                st.add(nums[i])
