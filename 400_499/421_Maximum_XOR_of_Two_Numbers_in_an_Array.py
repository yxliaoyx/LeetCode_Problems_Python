class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask = result = 0

        for i in range(max(nums).bit_length() - 1, -1, -1):
            seen = set()

            mask |= 1 << i
            current_max = result | (1 << i)

            for n in nums:
                prefix = n & mask

                if (prefix ^ current_max) in seen:
                    result = current_max
                    break

                seen.add(prefix)

        return result
