import argparse


def add_numbers(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def main() -> None:
    parser = argparse.ArgumentParser(description="Add two numbers.")
    parser.add_argument("--a", type=float, default=2, help="First number")
    parser.add_argument("--b", type=float, default=3, help="Second number")
    args = parser.parse_args()

    print(f"Sum: {add_numbers(args.a, args.b)}")


if __name__ == "__main__":
    main()
