class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score, left, right = 0, 0, len(tokens) - 1

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
            elif score and left < right:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break

        return score
