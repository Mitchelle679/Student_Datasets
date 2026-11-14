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

student_details = {
    "Name": "Iyamu Irenonsen Mitchelle",
    "Matric Number": "24/13610",
    "Department": "Computer Science",
    "Course Code": "CUL-CYB371",
    "Level": "300",
}

total_students = len(students)
total_attendance = sum(student["attendance_percentage"] for student in students)
total_score = sum(student["avg_exam_score"] for student in students)
class_avg_attendance = total_attendance / total_students
class_avg_score = total_score / total_students


def print_table(headers, rows):
    widths = [len(str(header)) for header in headers]
    for row in rows:
        for index, value in enumerate(row):
            widths[index] = max(widths[index], len(str(value)))

    border = "+-" + "-+-".join("-" * width for width in widths) + "-+"
    print(border)
    print("| " + " | ".join(f"{str(header):<{widths[index]}}" for index, header in enumerate(headers)) + " |")
    print(border)
    for row in rows:
        print("| " + " | ".join(f"{str(value):<{widths[index]}}" for index, value in enumerate(row)) + " |")
    print(border)


student_rows = [
    [
        student["student_id"],
        student["department"],
        student["level"],
        f"{student['attendance_percentage']}%",
        student["avg_exam_score"],
    ]
    for student in students
]

student_detail_rows = [[key, value] for key, value in student_details.items()]
print("Student Performance Dataset")
print_table(["Student ID", "Department", "Level", "Attendance %", "Avg Exam Score"], student_rows)
