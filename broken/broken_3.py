# broken_3.py — Fix the TypeError
#
# Run this file: python broken/broken_3.py
# Read the traceback. Then fix the bug and run again until it exits with no errors.
#
# Hint: A TypeError means an operation was applied to a value of the wrong type.
# Hint: The `+` operator on strings does concatenation — both operands must be strings.
# Hint: To convert an integer to a string: str(value). Or use an f-string instead of +.


def format_report(label, value):
    return "Score — " + label + ": " + str(value)


if __name__ == "__main__":
    print(format_report("Alice", 92))
