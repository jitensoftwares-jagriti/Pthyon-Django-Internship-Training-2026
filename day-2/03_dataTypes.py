# /d:/Code Playground/python_and_django/day-2/03_dataTypes1.py
# A tiny, slightly silly tour of common Python built-in data types.

def show(name, value, joke=""):
	print(f"{name:10} ({type(value).__name__:10}): {value!r}  — {joke}")

def example_function(x): return x * 2

def main():
	examples = [
		("None",        None,                         "The mysterious null guest."),
		("bool",        True,                         "Yes/no, true/false, dramatic decisions."),
		("int",         42,                           "The answer to everything."),
		("float",       3.14159,                      "Pi: irrationally popular."),
		("complex",     2-3j,                         "When regular numbers get moody."),
		("str",         "Hello, world!",              "Text that talks back."),
		("bytes",       b'binary',                    "Tiny, silent bytes."),
		("bytearray",   bytearray(b'mutable'),        "Bytes that can change their mind."),
		("memoryview",  memoryview(b'peek'),          "A window into bytes."),
		("list",        [1, 2, 3],                    "Ordered, mutable troupe."),
		("tuple",       (1, 2, 3),                    "Ordered, immutable statues."),
		("range",       range(5),                     "Lazy sequence — saves energy."),
		("dict",        {'a': 1, 'b': 2},             "Key-value gossip."),
		("set",         {1, 2, 3},                    "Unique party guests."),
		("frozenset",   frozenset([1, 2, 3]),         "Frozen set: rules are strict."),
		("slice",       slice(1, 5, 2),               "Slice: cake for indices."),
		("function",    example_function,             "Callable: asks for input, returns drama."),
		("type",        type,                         "The meta-type."),
	]

	print("\nPython built-in type showcase (with a wink):\n")
	for name, val, joke in examples:
		show(name, val, joke)

	# Quick tiny demos for a couple of interactive behaviors
	print("\nQuick demos:")
	print("  list + [4]    ->", [1,2,3] + [4])
	print("  tuple * 2     ->", (1,2) * 2)
	print("  set add 4     ->", end=" ")
	s = {1,2,3}
	s.add(4)
	print(s)
	print("  bytes[0]      ->", b'hi'[0], "(an int, surprise!)")
	print("  bytearray[0]=120 ->", end=" ")
	ba = bytearray(b'ab')
	ba[0] = 120
	print(ba)

if __name__ == "__main__":
	main()