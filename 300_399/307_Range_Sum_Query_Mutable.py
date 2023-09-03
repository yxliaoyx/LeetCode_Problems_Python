class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.nums_sum = sum(nums)

    def update(self, index: int, val: int) -> None:
        self.nums_sum += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.nums_sum - sum(self.nums[0:left]) - sum(self.nums[right + 1:])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
