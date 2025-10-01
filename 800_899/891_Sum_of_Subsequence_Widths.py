class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        answer = 0
        pow2 = 1

        nums.sort()

        for i in range(len(nums)):
            answer += (nums[i] - nums[~i]) * pow2
            pow2 = pow2 * 2 % 1_000_000_007

        return answer % 1_000_000_007
