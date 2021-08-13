import sys


class Dog:
    pass


buddy = Dog()
buddy.name = "Rex"
buddy.bread = "Rottweiler"

print(buddy.__dict__)


class Point:
    __slots__ = ("x", "y")


point = Point()
point.x = 5
point.y = 7

try:
    point.name = "Fred"
except AttributeError as e:
    print("Point does not have a name attribute")

list_size = sys.getsizeof(list())
set_size = sys.getsizeof(set())
dict_size = sys.getsizeof(dict())
tuple_size = sys.getsizeof(tuple())

print(f"List size: {list_size} bytes")
print(f"Set size: {set_size} bytes")
print(f"Dict size: {dict_size} bytes")
print(f"Tuple size: {tuple_size} bytes")
