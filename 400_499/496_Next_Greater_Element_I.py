class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        stack = []

        for i in nums2:
            while stack and stack[-1] < i:
                mapping[stack.pop()] = i

            stack.append(i)

        return [mapping.get(i, -1) for i in nums1]
