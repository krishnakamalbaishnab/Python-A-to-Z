# Define two numbers
a = 5   # 0b0101 in binary
b = 3   # 0b0011 in binary

# Bitwise Complement (~)
comp_a = ~a  # Inverts all bits of 'a'
print(f"Complement of {a} (~a): {comp_a}")

# Bitwise AND (&)
and_result = a & b  # Performs bitwise AND operation
print(f"{a} & {b} = {and_result}")

# Bitwise OR (|)
or_result = a | b  # Performs bitwise OR operation
print(f"{a} | {b} = {or_result}")

# Bitwise XOR (^)
xor_result = a ^ b  # Performs bitwise XOR operation
print(f"{a} ^ {b} = {xor_result}")

# Left Shift (<<)
left_shift = a << 1  # Shifts bits of 'a' to the left by 1 position
print(f"{a} << 1 = {left_shift}")

# Right Shift (>>)
right_shift = a >> 1  # Shifts bits of 'a' to the right by 1 position
print(f"{a} >> 1 = {right_shift}")





# TODO: Explanation:
# Complement (~a): Inverts all bits (one's complement).
# AND (a & b): Performs bitwise AND operation.
# OR (a | b): Performs bitwise OR operation.
# XOR (a ^ b): Performs bitwise XOR operation (1 if bits are different).
# Left Shift (a << n): Moves bits to the left, multiplying by 2^n.
# Right Shift (a >> n): Moves bits to the right, dividing by 2^n.