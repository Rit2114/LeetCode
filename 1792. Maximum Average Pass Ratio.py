class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n=len(classes)
        sum=0
        A=[]
        for p,q in classes:
            sum+=p/q
            A.append(((p-q)/(q*(q+1)), p, q)) # change sign
            
        heapify(A)

