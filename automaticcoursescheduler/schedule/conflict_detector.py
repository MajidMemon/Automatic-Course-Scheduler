# conflict_detector.py


class ScheduleConflictDetector:
    def __init__(self, schedule):
        self.schedule = schedule

    def detect_conflicts(self):
        conflicts = []
        classroom_conflicts = 0
        instructor_conflicts = 0

        for i in range(len(self.schedule)):
            for j in range(i + 1, len(self.schedule)):
                if (
                    self.schedule[i][3] == self.schedule[j][3] and  # Check classroom conflict
                    self.schedule[i][5] == self.schedule[j][5] and  # Check timing conflict
                    self.schedule[i][4] != self.schedule[j][4]  # Ensure different instructors
                ):
                    conflicts.append((
                        self.schedule[i][0], self.schedule[j][0],  # Serial numbers of conflicting classes
                        "Classroom Conflict",
                        f"Serial Numbers: {self.schedule[i][0]} and {self.schedule[j][0]}",
                        f"Conflict: Single classroom assigned to two different courses/instructor at the same time.",
                        f"Classroom: {self.schedule[i][3]}, Time: {self.schedule[i][5]}",
                        f"Course 1: {self.schedule[i][1]} - {self.schedule[i][2]}, Instructor: {self.schedule[i][4]}",
                        f"Course 2: {self.schedule[j][1]} - {self.schedule[j][2]}, Instructor: {self.schedule[j][4]}"
                    ))
                    classroom_conflicts += 1

                if (
                    self.schedule[i][4] == self.schedule[j][4] and  # Check instructor conflict
                    self.schedule[i][5] == self.schedule[j][5] and  # Check timing conflict
                    self.schedule[i][3] != self.schedule[j][3]  # Ensure different classrooms
                ):
                    conflicts.append((
                        self.schedule[i][0], self.schedule[j][0],  # Serial numbers of conflicting classes
                        "Instructor Conflict",
                        f"Serial Numbers: {self.schedule[i][0]} and {self.schedule[j][0]}",
                        f"Conflict: Single instructor assigned to two different classrooms at the same time.",
                        f"Instructor: {self.schedule[i][4]}, Time: {self.schedule[i][5]}",
                        f"Course 1: {self.schedule[i][1]} - {self.schedule[i][2]}, Classroom: {self.schedule[i][3]}",
                        f"Course 2: {self.schedule[j][1]} - {self.schedule[j][2]}, Classroom: {self.schedule[j][3]}"
                    ))
                    instructor_conflicts += 1

        summary = f"Summary:\nClassroom Conflicts: {classroom_conflicts}\nInstructor Conflicts: {instructor_conflicts}"
        return conflicts, summary
