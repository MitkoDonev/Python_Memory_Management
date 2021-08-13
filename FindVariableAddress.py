number1 = 30
number2 = 50
number3 = 1

number1_memory_address = id(number1)
number2_memory_address = id(number2)
number3_memory_address = id(number3)

print(
    f"Memory Adress:\nNumber1: {number1_memory_address}\nNumber2: {number2_memory_address}\nNumber3: {number3_memory_address}\n"
)

number1_address_to_hex = hex(number1_memory_address)
number2_address_to_hex = hex(number2_memory_address)
number3_address_to_hex = hex(number3_memory_address)


print(
    f"Memory Adress as HEX:\nNumber1: {number1_address_to_hex}\nNumber2: {number2_address_to_hex}\nNumber3: {number3_address_to_hex}\n"
)

print("Overrite value in same memory location\n")

number1 = 100
number1_memory_address = id(number1)

print(f"Memory Adress:\nNumber1: {number1_memory_address}")

number1_address_to_hex = hex(number1_memory_address)

print(f"Memory Adress as HEX:\nNumber1: {number1_address_to_hex}")
