
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        diagonals = [[] for _ in range(rows + cols - 1)]
