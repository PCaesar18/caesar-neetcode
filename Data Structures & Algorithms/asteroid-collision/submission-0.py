class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for rock in asteroids:
            while stack and rock < 0 and stack[-1] > 0:
                difference = rock + stack[-1]
                if difference < 0:
                    stack.pop()
                elif difference > 0:
                    rock = 0
                else:
                    rock = 0
                    stack.pop()
            if rock:
                stack.append(rock)
        return stack 
        