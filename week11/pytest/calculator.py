from week11.pytest.mypackage.calculator_API import add, subtract, divide, is_prime, factorial, power, multiply

def print_menu():
    print("\n========= Calculator =========")
    print("1. Addition (A + B)")
    print("2. Subtraction (A - B)")
    print("3. Multiplication (A * B)")
    print("4. Division (A / B)")
    print("5. Factorial")
    print("6. Power Calculation")
    print("7. Is a prime number")
    print("8. Numbers")
    print("9. Exit")

def print_invalid_choice():
    print("Invalid choice. Please try again.")

def print_invalid_count_of_numbers():
    print("Invalid choice. Please try again.")

def input_two_numbers():
    a = int(input("Input A: "))
    b = int(input("Input B: "))
    return a, b

def input_one_number():
    return int(input("Input a number: "))

def input_numbers():
    numbers = input("Input numbers: ")
    numbers = numbers.split(",")
    return numbers

def main():
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == '1':
            a, b = input_two_numbers()
            print(add(a, b))
        elif choice == '2':
            a, b = input_two_numbers()
            print(subtract(a, b))
        elif choice == '3':
            a, b = input_two_numbers()
            print(multiply(a, b))
        elif choice == '4':
            a, b = input_two_numbers()
            print(divide(a, b))
        elif choice == '5':
            a = input_one_number()
            print(factorial(a))
        elif choice == '6':
            a = input_one_number()
            print(is_prime(a))
        elif choice == '7':
            a, b = input_two_numbers()
            print(power(a, b))
        elif choice == '8':
            numbers = input_numbers()
            if len(numbers) == 1:
                print(factorial(int(numbers[0])))
            elif len(numbers) == 2:
                print(power(int(numbers[0]), int(numbers[1])))
            else:
                print_invalid_count_of_numbers()

        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print_invalid_choice()

if __name__ == "__main__":
    main()