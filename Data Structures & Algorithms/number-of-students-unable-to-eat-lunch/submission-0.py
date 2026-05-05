class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 1. Count how many students want 0 and how many want 1
        from collections import Counter
        counts = Counter(students)
        
        # 2. Iterate through the sandwiches in order
        for s in sandwiches:
            # If there's a student who wants this sandwich, they will 
            # eventually get to the front and take it.
            if counts[s] > 0:
                counts[s] -= 1
            else:
                # If NO ONE left wants this sandwich, the line stops.
                break
        
        # 3. The remaining counts are the students who couldn't eat
        return counts[0] + counts[1]