class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []

        for num in arr:
            if stack and stack[-1] > num:
                max_in_stack = stack.pop()

                while stack and stack[-1] > num:
                    stack.pop()

                stack.append(max_in_stack)
            else:
                stack.append(num)

        return len(stack)
