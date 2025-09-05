class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        if num1 == 0:
            return 0

        for t in range(0, 61):  # 0..60
            s = num1 - t * num2
            if s < 0:
                continue
            if s < t:
                continue

      
