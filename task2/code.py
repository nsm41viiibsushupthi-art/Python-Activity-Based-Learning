students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nStudent {i + 1}")
    name = input("Name: ")
    marks = float(input("Aggregate marks (%): "))
    subject_marks = list(map(float, input(
        "Enter marks in 3 subjects: "
    ).split()))
    attendance = float(input("Attendance (%): "))
    income = float(input("Family income (Rs): "))

    if (marks >= 75 and min(subject_marks) >= 60
            and attendance >= 75 and income <= 200000):
        students.append({
            "name": name,
            "marks": marks,
            "attendance": attendance,
            "income": income
        })

students.sort(
    key=lambda s: (
        -s["marks"], -s["attendance"], s["income"]
    )
)

print("\nEligible Scholarship Students")
if students:
    for rank, s in enumerate(students, start=1):
        print(
            rank, s["name"],
            "- Marks:", s["marks"],
            "Attendance:", s["attendance"],
            "Income:", s["income"]
        )
else:
    print("No el
