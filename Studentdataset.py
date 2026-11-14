students = [
    {
        "student_id": "24/13512",
        "department": "Computer Science",
        "level": 300,
        "attendance_percentage": 88.5,
        "avg_exam_score": 76.4,
    },
    {
        "student_id": "24/14005",
        "department": "Computer Science",
        "level": 300,
        "attendance_percentage": 92.0,
        "avg_exam_score": 84.2,
    },
    {
        "student_id": "24/15103",
        "department": "Computer Science",
        "level": 300,
        "attendance_percentage": 75.0,
        "avg_exam_score": 65.0,
    },
    {
        "student_id": "24/14012",
        "department": "Computer Science",
        "level": 300,
        "attendance_percentage": 95.0,
        "avg_exam_score": 91.5,
    },
]

print("Student Performance Dataset")
print("Student ID | Department       | Level | Attendance % | Avg Exam Score")
print("-" * 72)

for student in students:
    print(
        f"{student['student_id']:<10} | "
        f"{student['department']:<16} | "
        f"{student['level']:<5} | "
        f"{student['attendance_percentage']:<12} | "
        f"{student['avg_exam_score']}"
    )

