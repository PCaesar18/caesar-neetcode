class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        prefer = defaultdict(int)

        for student in students:
            prefer[student] += 1
        for sandwich in sandwiches:
            if prefer[sandwich] > 0:
                prefer[sandwich] -= 1
            else:
                return sum(prefer.values())

        return 0



        
        