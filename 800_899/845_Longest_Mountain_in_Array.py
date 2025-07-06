class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        longest = 0

        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left = i - 1
                while left >= 0 and arr[left] < arr[left + 1]:
                    left -= 1

                right = i + 1
                while right < len(arr) and arr[right] < arr[right - 1]:
                    right += 1

                longest = max(longest, right - left - 1)

        return longest
