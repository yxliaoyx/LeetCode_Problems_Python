class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Alice can always win with an even number of piles.
        # She can always choose either all the even indexed piles or all the odd indexed piles.
        return True
