class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        last = other = -1
        last_run = count = total = 0

        for f in fruits:
            count = count + 1 if f in (last, other) else last_run + 1

            if f == last:
                last_run += 1
            else:
                last_run = 1
                other, last = last, f

            total = max(total, count)

        return total
