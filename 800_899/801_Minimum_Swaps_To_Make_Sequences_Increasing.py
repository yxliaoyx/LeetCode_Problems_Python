class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        no_swap, swap = 0, 1

        for i in range(1, len(nums1)):
            prev_no_swap, prev_swap = no_swap, swap
            no_swap = swap = float("inf")

            if nums1[i - 1] < nums1[i] and nums2[i - 1] < nums2[i]:
                no_swap = min(no_swap, prev_no_swap)
                swap = min(swap, prev_swap + 1)
            if nums1[i - 1] < nums2[i] and nums2[i - 1] < nums1[i]:
                no_swap = min(no_swap, prev_swap)
                swap = min(swap, prev_no_swap + 1)

        return min(no_swap, swap)
