class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(k):
            if k < 2:
                return False
            for i in range(2, int(k**0.5) + 1):
                if k % i == 0:
                    return False
            return True

        if 8 <= n <= 11:
            return 11

        for num in range(10 ** (len(str(n)) // 2), 10**5):
            palindrome = int(str(num) + str(num)[-2::-1])
            if palindrome >= n and is_prime(palindrome):
                return palindrome
