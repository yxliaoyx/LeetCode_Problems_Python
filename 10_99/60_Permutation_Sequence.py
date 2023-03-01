class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        factorial = [1] * n
        result = []

        k -= 1

        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i

        for i in range(n - 1, -1, -1):
            index, k = divmod(k, factorial[i])

            result.append(nums[index])
            nums.pop(index)

        return ''.join(result)
