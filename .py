class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        return [*map(lambda d:max(d.values())-d[-1]+1
