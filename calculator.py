def calculate(first_number, operator, second_number):
    """Perform a basic arithmetic operation."""
    if operator == "+":
        return first_number + second_number
    if operator == "-":
        return first_number - second_number
    if operator == "*":
        return first_number * second_number
    if operator == "/":
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number / second_number
    raise ValueError("Unsupported operator. Use +, -, *, or /.")


def main():
    print("Simple Calculator")
    print("Enter q at the first number prompt to quit.")

    while True:
        first_input = input("\nFirst number: ").strip()
        if first_input.lower() == "q":
            print("Goodbye!")
            break

        try:
            first_number = float(first_input)
            operator = input("Operator (+, -, *, /): ").strip()
            second_number = float(input("Second number: "))
            result = calculate(first_number, operator, second_number)
        except ValueError as error:
            print(f"Invalid input: {error}")
            continue
        except ZeroDivisionError as error:
            print(error)
            continue

        print(f"Result: {result:g}")


if __name__ == "__main__":
    main()
