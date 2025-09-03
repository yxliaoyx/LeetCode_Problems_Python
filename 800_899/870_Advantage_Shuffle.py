from collections import deque


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        q = deque(sorted(nums1))
        result = [0] * len(nums1)

        for i in sorted(range(len(nums1)), key=lambda x: nums2[x], reverse=True):
            if q[-1] > nums2[i]:
                result[i] = q.pop()
            else:
                result[i] = q.popleft()

        return result
