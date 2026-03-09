# Day-10_PM/part_a.py
from collections import defaultdict
from typing import List, Dict


def create_student(name: str, roll: str, **marks) -> dict:
    """
    Create a student record.

    Args:
        name: Student name
        roll: Roll number
        **marks: Subject marks as keyword arguments

    Returns:
        dict: Student record
    """
    return {
        "name": name,
        "roll": roll,
        "marks": marks,
        "attendance": 0.0
    }


def calculate_gpa(*marks: float, scale: float = 10.0) -> float:
    """
    Calculate GPA from marks.

    Args:
        *marks: Any number of marks
        scale: GPA scale

    Returns:
        float: GPA value
    """
    if not marks:
        return 0.0

    avg = sum(marks) / len(marks)
    return round((avg / 100) * scale, 2)


def get_top_performers(students: List[Dict], n: int = 5, subject: str = None) -> List[Dict]:
    """
    Get top performing students.

    Args:
        students: List of student dictionaries
        n: number of top students
        subject: specific subject ranking

    Returns:
        list of students
    """
    if not students:
        return []

    if subject:
        ranked = sorted(students, key=lambda s: s["marks"].get(subject, 0), reverse=True)
    else:
        ranked = sorted(
            students,
            key=lambda s: sum(s["marks"].values()) / len(s["marks"]),
            reverse=True
        )

    return ranked[:n]


def generate_report(student: Dict, **options) -> str:
    """
    Generate formatted student report.

    Args:
        student: student dictionary
        **options: include_rank, include_grade, verbose

    Returns:
        str report
    """
    include_rank = options.get("include_rank", True)
    include_grade = options.get("include_grade", True)

    marks = student.get("marks", {})
    avg = sum(marks.values()) / len(marks)

    report = f"Student: {student['name']} ({student['roll']})\n"
    report += f"Average: {avg:.2f}\n"

    if include_grade:
        if avg >= 85:
            grade = "A"
        elif avg >= 70:
            grade = "B"
        elif avg >= 55:
            grade = "C"
        else:
            grade = "D"

        report += f"Grade: {grade}\n"

    return report


def classify_students(students: List[Dict]) -> Dict:
    """
    Classify students into grade groups.

    Returns:
        dict with A/B/C/D groups
    """
    groups = defaultdict(list)

    for s in students:
        marks = s.get("marks", {})
        avg = sum(marks.values()) / len(marks)

        if avg >= 85:
            groups["A"].append(s)
        elif avg >= 70:
            groups["B"].append(s)
        elif avg >= 55:
            groups["C"].append(s)
        else:
            groups["D"].append(s)

    return dict(groups)


# Example usage
students = [
    create_student("Amit", "R001", math=85, python=92, ml=78),
    create_student("Priya", "R002", math=95, python=88, ml=91),
]

print(calculate_gpa(85, 92, 78))
print(get_top_performers(students, n=1, subject="python"))