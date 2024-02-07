class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()

        def backtrack(start, path):
            if len(path) > 1:
                result.add(tuple(path))

            for i in range(start, len(nums)):
                if not path or path[-1] <= nums[i]:
                    backtrack(i + 1, path + [nums[i]])

        backtrack(0, [])

        return result
