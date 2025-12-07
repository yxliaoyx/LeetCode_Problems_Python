class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        xs = [1] if x == 1 else [x**i for i in range(20) if x**i <= bound]
        ys = [1] if y == 1 else [y**i for i in range(20) if y**i <= bound]
        return list({a + b for a in xs for b in ys if a + b <= bound})
