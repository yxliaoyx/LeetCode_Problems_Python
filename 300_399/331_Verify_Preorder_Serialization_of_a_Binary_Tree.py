class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slot = 1

        for node in preorder.split(','):
            if slot == 0:
                return False

            if node == '#':
                slot -= 1
            else:  # occupy one slot but create two new slots
                slot += 1

        return slot == 0
