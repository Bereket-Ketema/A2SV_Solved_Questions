class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            digits = list(map(int, str(n)))
            n = sum(map(lambda x: x * x, digits))
        
        return n == 1
