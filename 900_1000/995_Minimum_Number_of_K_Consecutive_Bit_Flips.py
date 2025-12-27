class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        answer = count = 0

        for i in range(len(nums)):
            if i >= k and nums[i - k] > 1:
                count -= 1

            if (nums[i] + count) % 2 == 0:
                if i + k > len(nums):
                    return -1

                nums[i] = 2
                count += 1
                answer += 1

        return answer
