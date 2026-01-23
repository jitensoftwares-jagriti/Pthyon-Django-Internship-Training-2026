# Initial task list creation
tasks = []
# empty list

# 1️⃣ append() – add tasks
tasks.append("Login Feature")
tasks.append("Signup Feature")

# 2️⃣ extend() – add multiple tasks
tasks.extend(["Profile Page", "Logout Feature"])

# 3️⃣ insert() – insert a high priority task at the beginning
tasks.insert(0, "Database Setup")

print("After adding tasks:", tasks)


# 4️⃣ remove() – remove a completed task
tasks.remove("Signup Feature")

# 5️⃣ pop() – remove the last task and store it
last_task = tasks.pop()
print("Last removed task:", last_task)

print("After removals:", tasks)


# Adding duplicate tasks intentionally
tasks.append("Login Feature")
tasks.append("Profile Page")

print("With duplicates:", tasks)


# 6️⃣ index() – find position of a task
login_index = tasks.index("Login Feature")
print("Index of Login Feature:", login_index)

# 7️⃣ count() – count occurrences of a task
login_count = tasks.count("Login Feature")
print("Login Feature count:", login_count)


# 8️⃣ sort() – sort tasks alphabetically
tasks.sort()
print("Sorted tasks:", tasks)

# 9️⃣ reverse() – reverse task order
tasks.reverse()
print("Reversed tasks:", tasks)


# 🔟 copy() – create a backup before clearing
backup_tasks = tasks.copy()

# 1️⃣1️⃣ clear() – clear all tasks
tasks.clear()

print("Current tasks:", tasks)
print("Backup tasks:", backup_tasks)
