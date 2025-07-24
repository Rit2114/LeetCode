class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
      n=len(N);g=[[]for _ in N]
     for u,v in E:g[u]+=[v];g[v]+=[u]
     s=[0]*n;d=[0]*n
     def D(u,p):
      s[u],d[u]=N[u],1<<u
      for v in g[u]:
       if v-p:D(v,u);s[u]^=s[v];d[u]|=d[v]
     D(0,-1)
     r,t=9e9,s[0]
