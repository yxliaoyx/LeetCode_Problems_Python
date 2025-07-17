import bisect


class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.students = []

    def seat(self) -> int:
        if not self.students:
            seat_pos = 0
        else:
            max_dist = self.students[0]
            seat_pos = 0

            for i in range(1, len(self.students)):
                gap = (self.students[i] - self.students[i - 1]) // 2
                if gap > max_dist:
                    max_dist = gap
                    seat_pos = self.students[i - 1] + gap

            if self.n - 1 - self.students[-1] > max_dist:
                seat_pos = self.n - 1

        bisect.insort(self.students, seat_pos)
        return seat_pos

    def leave(self, p: int) -> None:
        self.students.remove(p)
