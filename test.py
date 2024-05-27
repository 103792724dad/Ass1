def find_failing_values(B):
    """
    Finds all values of A for a given B where the test cases (A, B) fail
    to detect any incorrect use of arithmetic operators in the program.

    Args:
        B: The value of the input variable B.

    Returns:
        A list of failing A values.
    """
    failing_values = []

    for A in range(-100, 101):  # Adjust the range if needed
        correct_C = (A - B) * 2
        for op1 in ["+", "/", "*"]:  # Incorrect operators for A = A - B
            for op2 in ["+", "-", "/"]:  # Incorrect operators for C = A * 2
                if eval(f"({A} {op1} {B}) {op2} 2") == correct_C:
                    failing_values.append(A)
                    break  # No need to check other op2 for this A

    return failing_values

if __name__ == "__main__":
    B = 1
    failing_A_values = find_failing_values(B)
    print(f"For B = {B}, the following A values fail to detect errors:")
    if failing_A_values:
        print(failing_A_values)
    else:
        print("None")