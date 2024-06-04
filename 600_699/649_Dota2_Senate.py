from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()

        for i, s in enumerate(senate):
            if s == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + len(senate))
            else:
                dire.append(dire[0] + len(senate))

            radiant.popleft()
            dire.popleft()

        return "Radiant" if radiant else "Dire"
