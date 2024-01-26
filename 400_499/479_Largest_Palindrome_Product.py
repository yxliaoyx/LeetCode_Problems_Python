from math import sqrt


class Solution:
    def largestPalindrome(self, n: int) -> int:
        upper = pow(10, n) - 1
        lower = pow(10, n - 1)

        for i in range(upper, lower - 1, -1):
            palindrome = int(str(i) + str(i)[::-1])

            for j in range(upper, int(sqrt(palindrome)), -1):
                if palindrome % j == 0:
                    return palindrome % 1337

        return 9
