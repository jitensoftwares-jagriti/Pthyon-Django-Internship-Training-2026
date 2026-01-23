students = [("Simran", 85), ("Megha", 92), ("Raghav", 78)]

sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)
# Sorts students by marks, not name.
# Lambda tells Python what exactly to look at while sorting.