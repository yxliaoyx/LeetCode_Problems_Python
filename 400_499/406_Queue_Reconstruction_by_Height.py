class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        queue = []

        for person in sorted(people, key=lambda x: (-x[0], x[1])):
            queue.insert(person[1], person)

        return queue
