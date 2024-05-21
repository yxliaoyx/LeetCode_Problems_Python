class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exclusive = [0] * n
        prev_time = 0
        stack = []

        for log in logs:
            function_id, status, timestamp = log.split(":")
            timestamp = int(timestamp)

            if stack:
                exclusive[stack[-1]] += timestamp - prev_time

            if status == "start":
                stack.append(int(function_id))
            else:
                exclusive[stack.pop()] += 1
                timestamp += 1

            prev_time = timestamp

        return exclusive
