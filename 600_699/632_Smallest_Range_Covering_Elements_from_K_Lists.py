import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        priority_queue = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(priority_queue)
        right = max(row[0] for row in nums)
        result = [priority_queue[0][0], right]

        while True:
            num, i, j = heapq.heappop(priority_queue)
            if j + 1 == len(nums[i]):
                return result

            heapq.heappush(priority_queue, (nums[i][j + 1], i, j + 1))
            right = max(right, nums[i][j + 1])

            if right - priority_queue[0][0] < result[1] - result[0]:
                result = [priority_queue[0][0], right]
