import sys

x = 300

y = 300

z = [300, 300]

reference_count_x = sys.getrefcount(id(x))

reference_count_y = sys.getrefcount(id(y))

reference_count_z = sys.getrefcount(id(z))

print(
    f"Reference count for X: {reference_count_x}\nReference count for Y: {reference_count_y}\nReference count for Z: {reference_count_z}"
)


def memory_test():
    num1 = 200
    num2 = 200

    num1_momery_id = id(num1)
    num2_momery_id = id(num2)

    hex_num1_memory = hex(num1_momery_id)
    hex_num2_memory = hex(num2_momery_id)

    print(f"Num1 memory ID: {num1_momery_id} / HEX: {hex_num1_memory}")
    print(f"Num2 memory ID: {num2_momery_id} / HEX: {hex_num2_memory}")
    print(f"Check if both operands refer to same object: {num1 is num2}")
    print(
        f"Compare address values equality of both operands: {num1_momery_id == num2_momery_id}"
    )


memory_test()
