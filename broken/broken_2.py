# broken_2.py — Fix the NameError
#
# Run this file: python broken/broken_2.py
# Read the traceback. Then fix the bug and run again until it exits with no errors.
#
# Hint: A NameError means Python encountered a name it has never seen before.
# Hint: Python is case-sensitive — `result` and `reslt` and `Result` are three different names.
# Hint: The last line of the traceback tells you the exact name Python could not find.


def compute_total(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    result = compute_total(data)
    print(f"Total: {result}")
