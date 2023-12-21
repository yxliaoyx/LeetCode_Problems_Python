class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        result = 0

        while i < len(chars):
            count = 1

            while i + count < len(chars) and chars[i + count] == chars[i]:
                count += 1

            chars[result] = chars[i]
            result += 1

            if count > 1:
                chars[result: result + len(str(count))] = str(count)
                result += len(str(count))

            i += count

        return result
