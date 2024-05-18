import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        heap = []
        time = 0

        for duration, end in courses:
            time += duration
            heapq.heappush(heap, -duration)

            if time > end:
                time += heapq.heappop(heap)

        return len(heap)
