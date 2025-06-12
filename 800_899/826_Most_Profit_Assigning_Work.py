class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        jobs = sorted(zip(difficulty, profit))

        max_profit = 0
        total = 0
        j = 0

        for ability in worker:
            while j < len(jobs) and ability >= jobs[j][0]:
                max_profit = max(max_profit, jobs[j][1])
                j += 1
            total += max_profit

        return total
