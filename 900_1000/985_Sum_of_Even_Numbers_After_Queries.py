class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(x for x in nums if x % 2 == 0)
        result = []

        for val, i in queries:
            if nums[i] % 2 == 0:
                even_sum -= nums[i]

            nums[i] += val

            if nums[i] % 2 == 0:
                even_sum += nums[i]

            result.append(even_sum)

        return result
