class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        answer = count = 0
        flipped = [0] * len(nums)

        for i, num in enumerate(nums):
            if i >= k:
                count -= flipped[i - k]

            if (num + count) % 2 == 0:
                if i + k > len(nums):
                    return -1

                flipped[i] = 1
                count += 1
                answer += 1

        return answer
