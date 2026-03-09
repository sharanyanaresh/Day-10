from collections import defaultdict

def merge_grade_reports(sem1, sem2):

    subjects = set(sem1.keys()) | set(sem2.keys())

    report = {}

    for subject in subjects:

        g1 = sem1.get(subject)
        g2 = sem2.get(subject)

        grades = [g for g in [g1, g2] if g is not None]

        combined_gpa = sum(grades) / len(grades)

        if g1 and g2:
            if g2 > g1:
                trend = "improving"
            elif g2 < g1:
                trend = "declining"
            else:
                trend = "stable"
        else:
            trend = "single semester"

        report[subject] = {
            "combined_gpa": combined_gpa,
            "trend": trend
        }

    common_subjects = set(sem1.keys()) & set(sem2.keys())

    return {
        "report": report,
        "common_subjects": list(common_subjects)
    }


sem1 = {"Math": 8.0, "Physics": 7.5, "CS": 9.0}
sem2 = {"Math": 8.5, "Physics": 7.0, "CS": 9.2, "AI": 8.8}

print(merge_grade_reports(sem1, sem2))