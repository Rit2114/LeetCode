class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        for i in range(n):
            x = nums[i]
            answer[i] = 1
            j = i - 1
