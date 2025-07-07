from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        card_count = Counter(hand)

        for card in sorted(card_count):
            if card_count[card] > 0:
                for i in range(1, groupSize):
                    if card_count[card + i] < card_count[card]:
                        return False
                    card_count[card + i] -= card_count[card]

        return True
