userInfo = {
    "id": 101,
    "name": "Darsh",
    "email": "darsh@gmail.com",
    "is_active": True,
    "age": 20
}


def demo_dict_methods():
    """Demonstrate common dict methods with `userInfo` for students.

    Each section prints a short explanation and the result so learners
    can see how the method behaves.
    """

    print('\n--- Original dict ---')
    print('userInfo =', userInfo)

    # copy(): returns a shallow copy of the dictionary
    print('\n--- copy() ---')
    copied = userInfo.copy()
    print('copied =', copied)
    copied['name'] = 'Changed in copy'
    print('modify copied["name"] -> copied:', copied)
    print('original still:', userInfo)

    # fromkeys(): build a new dict from an iterable of keys
    print('\n--- fromkeys() ---')
    keys = ['a', 'b', 'c']
    fromkeys_dict = dict.fromkeys(keys, 0)
    print("dict.fromkeys(['a','b','c'], 0) ->", fromkeys_dict)

    # get(): fetch value safely with optional default
    print('\n--- get() ---')
    print("get('email') ->", userInfo.get('email'))
    print("get('phone', 'N/A') ->", userInfo.get('phone', 'N/A'))

    # items(), keys(), values(): iterate over pairs/keys/values
    print('\n--- items(), keys(), values() ---')
    print('items ->', list(userInfo.items()))
    print('keys  ->', list(userInfo.keys()))
    print('values->', list(userInfo.values()))

    # Use values() for an aggregate example (non-destructive)
    print('\nSum numeric values (example):')
    numeric_values = [v for v in userInfo.values() if isinstance(v, (int, float))]
    print('numeric values ->', numeric_values)
    print('sum ->', sum(numeric_values))

    # pop(): remove a key and return its value
    print('\n--- pop() ---')
    temp = userInfo.copy()  # operate on a copy to keep original intact
    popped_age = temp.pop('age', None)
    print("popped 'age' ->", popped_age)
    print('after pop ->', temp)

    # popitem(): remove and return last inserted (key, value) pair
    print('\n--- popitem() ---')
    temp2 = userInfo.copy()
    last_item = temp2.popitem()
    print('popitem() ->', last_item)
    print('after popitem ->', temp2)

    # setdefault(): return value if key exists, otherwise set and return default
    print('\n--- setdefault() ---')
    temp3 = userInfo.copy()
    country = temp3.setdefault('country', 'India')
    print("setdefault('country', 'India') ->", country)
    print('after setdefault ->', temp3)

    # update(): merge another mapping into the dict
    print('\n--- update() ---')
    temp4 = userInfo.copy()
    temp4.update({'email': 'darsh@new.com', 'is_active': False, 'role': 'student'})
    print("after update({'email':..., 'role':...}) ->", temp4)

    # clear(): remove all items from a dictionary
    print('\n--- clear() ---')
    temp5 = userInfo.copy()
    temp5.clear()
    print('after clear ->', temp5)

    print('\n--- End of demonstrations ---\n')


if __name__ == '__main__':
    demo_dict_methods()
