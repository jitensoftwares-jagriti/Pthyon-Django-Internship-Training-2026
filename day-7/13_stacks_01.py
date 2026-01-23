call_stack = []

call_stack.append("main()")
call_stack.append("login()")
call_stack.append("validate_user()")

print(call_stack)
print(call_stack.pop())
# function returns
print(call_stack.pop())

# Python internally does this
# We are just simulating it