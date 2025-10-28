from collections import Counter


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = Counter(arr)
        nums = sorted(count)
        answer = 0

        for i, num_i in enumerate(nums):
            for j, num_j in enumerate(nums[i:], i):
                num_k = target - num_i - num_j
                if num_k < num_j:
                    break
                if num_k in count:
                    count_i, count_j, count_k = count[num_i], count[num_j], count[num_k]

                    if num_i == num_j == num_k:
                        answer += count_i * (count_i - 1) * (count_i - 2) // 6
                    elif num_i == num_j:
                        answer += count_i * (count_i - 1) // 2 * count_k
                    elif num_j == num_k:
                        answer += count_i * count_j * (count_j - 1) // 2
                    else:
                        answer += count_i * count_j * count_k

        return answer % 1_000_000_007
