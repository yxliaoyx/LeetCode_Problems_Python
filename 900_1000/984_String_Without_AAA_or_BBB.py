class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if a > b:
            diff = a - b
            if diff > b:
                return "aab" * b + "a" * (diff - b)
            return "aab" * diff + "ab" * (b - diff)
        else:
            diff = b - a
            if diff > a:
                return "bba" * a + "b" * (diff - a)
            return "bba" * diff + "ba" * (a - diff)
