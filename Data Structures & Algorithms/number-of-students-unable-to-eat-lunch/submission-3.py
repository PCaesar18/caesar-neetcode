class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        count = 0
        circle = 0

        while q and circle < len(q):
            if q[0] == sandwiches[count]:
                q.popleft()
                count += 1
                circle = 0
            else:
                q.append(q.popleft())
                circle += 1
        return len(q)       
                




        