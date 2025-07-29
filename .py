class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        return [*map(lambda d:max(d.values())-d[-1]+1,accumulate(range(len(a)-1,-1,-1),
