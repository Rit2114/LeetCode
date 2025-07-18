class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n=len(nums)//3
        diff=[0]*(n+1)
        heapify(pqL:=[-x for x in nums[:n]])
        heapify(pqR:=nums[2*n:])
        Sum=sum(nums[:n])
        ans=Sum
        for i in range(n, 2*n+1):
            diff[i-n]=Sum
            x=nums[i]
            
        
