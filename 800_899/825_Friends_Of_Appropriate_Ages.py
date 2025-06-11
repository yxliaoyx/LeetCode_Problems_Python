from collections import Counter


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = Counter(ages)
        requests = 0

        for age_a, count_a in count.items():
            for age_b, count_b in count.items():
                if age_a * 0.5 + 7 >= age_b or age_a < age_b:
                    continue

                requests += count_a * count_b

                if age_a == age_b:
                    requests -= count_a

        return requests
