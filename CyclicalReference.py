import sys


class Node:
    def __init__(self, value):
        self.value = value

    def child(self, child):
        self.child = child


root = Node("root")
left = Node("left")
right = Node("right")

root_ref_count = sys.getrefcount(id(root))
left_ref_count = sys.getrefcount(id(left))
right_ref_count = sys.getrefcount(id(right))

print(
    f"Reference count:\nROOT: {root_ref_count}\nLEFT: {left_ref_count}\nRIGHT: {right_ref_count}"
)

root.child(left)
left.child(right)
right.child(left)

new_root_ref_count = sys.getrefcount(id(root))
new_left_ref_count = sys.getrefcount(id(left))
new_right_ref_count = sys.getrefcount(id(right))

print(
    f"Reference count:\nROOT: {new_root_ref_count}\nLEFT: {new_left_ref_count}\nRIGHT: {new_right_ref_count}"
)
