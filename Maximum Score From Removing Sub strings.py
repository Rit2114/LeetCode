class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        def solve(text: str, pattern: str, score: int):
            stack = []
            points = 0
            for char in text:
                if stack and stack[-1] == pattern[0] and char == pattern[1]:
                    stack.pop()
                    points += score
                else:
                    stack.append(char)
            return points, "".join(stack)
