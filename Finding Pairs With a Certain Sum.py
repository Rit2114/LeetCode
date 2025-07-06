class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums2)

    
    def count(self, tot: int) -> int:
        ans = 0
        for a in self.nums1:  
            ans += self.freq[tot - a]  # a + b = tot -> b = tot - a
        return ans
