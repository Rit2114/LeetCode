class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n, prev, cnt=len(nums), nums[0], 0
        diff=[0, 0]
        i=0
