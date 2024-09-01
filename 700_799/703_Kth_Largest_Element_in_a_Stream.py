from heapq import heapify, heappush, heappushpop


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)[:k]

        heapify(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heappush(self.nums, val)
        elif val > self.nums[0]:
            heappushpop(self.nums, val)

        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
