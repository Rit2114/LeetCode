class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n, prev, cnt=len(nums), nums[0], 0
        diff=[0, 0]
        i=0
        while i<n:
            while i<n and prev==nums[i]: i+=1
            if i==n: break
            bigger=1 if nums[i]>prev 
