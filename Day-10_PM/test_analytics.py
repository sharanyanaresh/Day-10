from part_a import *

s1 = create_student("Amit", "R001", math=80, python=90)
assert s1["name"] == "Amit"

assert calculate_gpa(80, 90) > 0

students = [
    create_student("A", "1", math=80, python=90),
    create_student("B", "2", math=60, python=70),
]

assert len(get_top_performers(students, 1)) == 1
assert "Student:" in generate_report(students[0])
assert isinstance(classify_students(students), dict)