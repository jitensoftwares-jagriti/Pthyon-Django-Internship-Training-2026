# 1️⃣ Empty list using []
students = []
print(students)

# 2️⃣ List with initial values
default_students = ["Aman", "Neha", "Ravi"]
print(default_students)

# 3️⃣ Using list() constructor with iterable
scores_from_tuple = list((85, 90, 78))
print(scores_from_tuple)

# 4️⃣ Using list() with string
letters = list("ABC")
print(letters)

# 5️⃣ Using list comprehension
squared_scores = [score * score for score in scores_from_tuple]
print(squared_scores)
