def add_numbers(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


if __name__ == "__main__":
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))
    print(f"Sum: {add_numbers(first, second)}")
