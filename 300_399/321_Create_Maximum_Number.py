class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def find_max(nums, length):
            stack = []

            for i, num in enumerate(nums):
                while stack and len(nums) - i + len(stack) > length and num > stack[-1]:
                    stack.pop()

                if len(stack) < length:
                    stack.append(num)

            return stack

        def merge(n1, n2):
            merged = []
            i = j = 0

            while i < len(n1) or j < len(n2):
                if i >= len(n1):
                    merged.append(n2[j])
                    j += 1
                elif j >= len(n2):
                    merged.append(n1[i])
                    i += 1
                elif n1[i:] > n2[j:]:
                    merged.append(n1[i])
                    i += 1
                else:
                    merged.append(n2[j])
                    j += 1

            return merged

        result = []

        for len_1 in range(max(0, k - len(nums2)), min(len(nums1), k) + 1):
            result = max(result, merge(find_max(nums1, len_1), find_max(nums2, k - len_1)))

        return result
