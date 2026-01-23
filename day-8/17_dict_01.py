user = {
    "id": 101,
    "name": "Amit",
    "email": "amit@gmail.com",
    "is_active": True,
}

print(user["name"])
# KeyError if key doesn’t exist
# alternative use get() method, which returns null
print(user.get('age'))