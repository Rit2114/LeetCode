class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
      n=len(N);g=[[]for _ in N]
     for u,v in E:g[u]+=[v];g[v]+=[u]
     s=[0]*n;d=[0]*n
     def D(u,p):
