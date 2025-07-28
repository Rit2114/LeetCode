class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        return (f:=lambda i,o,O=reduce(or_,a):a[i:]
