class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        n = len(points)
        result = 0

        for i in range(n):
            top = points[i][1]
            bot = float("-inf")
            

