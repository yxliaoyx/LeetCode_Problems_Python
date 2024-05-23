from functools import cache


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        @cache
        def dfs(current_needs):
            cost = sum(needs * cost for needs, cost in zip(current_needs, price))

            for offer in special:
                new_needs = [needs - offer for needs, offer in zip(current_needs, offer)]

                if min(new_needs) >= 0:
                    cost = min(cost, offer[-1] + dfs(tuple(new_needs)))

            return cost

        return dfs(tuple(needs))
