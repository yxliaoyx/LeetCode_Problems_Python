from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        q = deque()

        for card in sorted(deck, reverse=True):
            if q:
                q.appendleft(q.pop())
            q.appendleft(card)

        return list(q)
