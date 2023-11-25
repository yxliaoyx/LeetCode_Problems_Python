class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz, buzz, fizzbuzz = "Fizz", "Buzz", "FizzBuzz"
        answer = [str(x + 1) for x in range(n)]

        for i in range(2, n, 3):
            answer[i] = fizz

        for i in range(4, n, 5):
            answer[i] = buzz

        for i in range(14, n, 15):
            answer[i] = fizzbuzz

        return answer
