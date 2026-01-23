def create_profile(username, **details):
    print("Profile for:", username)

    if not details:
        print("No extra details provided 😶")
    else:
        print("Profile details:")
        for key, value in details.items():
            print(f"{key} : {value}")

create_profile("rahul_07")
create_profile(
    "priya_21",
    age=23,
    city="Mumbai",
    hobby="Photography"
)
