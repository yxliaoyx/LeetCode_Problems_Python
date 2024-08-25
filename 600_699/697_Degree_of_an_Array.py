class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}

        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i

            right[x] = i
            count[x] = count.get(x, 0) + 1

        degree = max(count.values())

        return min((right[x] - left[x] + 1) for x, cnt in count.items() if cnt == degree)
