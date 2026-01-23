actions = []

actions.append("type A")
actions.append("type B")
actions.append("delete B")

poppedItem = actions.pop()
print(poppedItem)
# undo last action
print(actions.pop())
# undo previous action
print(actions)