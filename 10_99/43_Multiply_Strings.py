class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        answer = [0] * (len(num1) + len(num2))

        for i, number_1 in enumerate(num1[::-1]):
            for j, number_2 in enumerate(num2[::-1]):
                position = j + i

                multiplication = int(number_2) * int(number_1) + answer[position]

                answer[position] = multiplication % 10
                answer[position + 1] += multiplication // 10

        if answer[-1] == 0:
            answer.pop()

        return ''.join(str(digit) for digit in reversed(answer))
