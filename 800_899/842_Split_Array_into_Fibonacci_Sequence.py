from typing import List


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        for i in range(1, min(11, len(num))):
            if num[0] == "0" and i > 1:
                break

            a = int(num[:i])
            for j in range(i + 1, min(i + 11, len(num) + 1)):
                if num[i] == "0" and j > i + 1:
                    break

                b = int(num[i:j])
                fibonacci = [a, b]
                k = j

                while k < len(num):
                    nxt = fibonacci[-1] + fibonacci[-2]
                    nxt_str = str(nxt)
                    if nxt > 2147483647 or not num.startswith(nxt_str, k):
                        break

                    fibonacci.append(nxt)
                    k += len(nxt_str)

                if k == len(num) and len(fibonacci) >= 3:
                    return fibonacci

        return []
