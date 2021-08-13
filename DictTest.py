random_dict = {}

random_dict[1] = "python"
random_dict[1.0] = "javascript"
random_dict[2 - 1] = "random_text"

tuple_key = ("tuple", 123)

random_dict[tuple_key] = "tuple_as_key"
random_dict[tuple_key[0]] = "tuple[0]_as_key"
random_dict[tuple_key[1]] = "tuple[1]_as_key"

print(random_dict)
