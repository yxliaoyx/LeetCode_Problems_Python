class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, len(citations) - 1

        while left < right:
            mid = (left + right) // 2

            if citations[mid] < len(citations) - mid:
                left = mid + 1
            else:
                right = mid

        return min(len(citations) - right, citations[right])
