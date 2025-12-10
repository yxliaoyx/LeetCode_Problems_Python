class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        def make_next(indices):
            result = [-1] * len(arr)
            stack = []

            for i in indices:
                while stack and stack[-1] < i:
                    result[stack.pop()] = i
                stack.append(i)

            return result

        large = make_next(sorted(range(len(arr)), key=lambda x: arr[x]))
        small = make_next(sorted(range(len(arr)), key=lambda x: -arr[x]))

        odd = [0] * len(arr)
        even = [0] * len(arr)
        odd[-1] = even[-1] = 1

        for i in range(len(arr) - 2, -1, -1):
            if large[i] > -1:
                odd[i] = even[large[i]]
            if small[i] > -1:
                even[i] = odd[small[i]]

        return sum(odd)
