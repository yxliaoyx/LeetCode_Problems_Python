class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_palindromes(left: int, right: int) -> int:
            count = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            return count

        return sum(count_palindromes(i, j) for i in range(len(s)) for j in (i, i + 1))
