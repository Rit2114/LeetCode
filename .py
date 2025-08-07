class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n=len(fruits)
        diag=0
        for i, row in enumerate(fruits):
            diag+=row[i]
        for i in range(n-2):
            fruits[i][n-2-i]=fruits[i][n-3-i]=0
        fruits[n-2][0]=0
