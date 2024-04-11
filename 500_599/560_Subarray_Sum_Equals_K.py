class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = num_sum = 0
        m = {0: 1}

        for num in nums:
            num_sum += num
            result += m.get(num_sum - k, 0)
            m[num_sum] = m.get(num_sum, 0) + 1

        return result
