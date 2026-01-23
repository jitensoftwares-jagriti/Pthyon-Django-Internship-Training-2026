from collections import deque

support_queue = deque()

support_queue.append("Customer A")
support_queue.append("Customer B")
support_queue.append("Customer C")

print(support_queue.popleft())
print(support_queue.popleft())
print(support_queue)