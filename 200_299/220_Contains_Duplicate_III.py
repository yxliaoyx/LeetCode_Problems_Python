class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {}
        bucket_size = valueDiff + 1

        for i, n in enumerate(nums):
            bucket_id = n // bucket_size

            if (
                    bucket_id in buckets or
                    bucket_id - 1 in buckets and abs(n - buckets[bucket_id - 1]) <= valueDiff or
                    bucket_id + 1 in buckets and abs(n - buckets[bucket_id + 1]) <= valueDiff
            ):
                return True

            buckets[bucket_id] = n

            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // bucket_size]

        return False
