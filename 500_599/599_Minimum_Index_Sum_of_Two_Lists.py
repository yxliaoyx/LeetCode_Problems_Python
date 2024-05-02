class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_restaurants = set(list1) & set(list2)

        index_sum_dic = {
            restaurant: list1.index(restaurant) + list2.index(restaurant) for restaurant in common_restaurants
        }

        min_index_sum = min(index_sum_dic.values())

        return [restaurant for restaurant, index_sum in index_sum_dic.items() if index_sum == min_index_sum]
