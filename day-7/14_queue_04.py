from collections import deque

tasks = deque()

tasks.append("low_priority_task")
tasks.append("medium_priority_task")

tasks.appendleft("high_priority_task")
print(tasks)

print(tasks.popleft())  # high priority first
print(tasks.popleft())
