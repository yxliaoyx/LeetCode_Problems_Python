class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        answer = []
        left, right = 1, n

        for i in range(k, 1, -1):
            if i % 2 == 0:
                answer.append(right)
                right -= 1
            else:
                answer.append(left)
                left += 1

        return answer + list(range(left, right + 1))
