# Python program for Part A and Part B questions

def sum_of_two_numbers():
    # This function takes two numbers from the user and prints their sum.
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Sum:", a + b)
    except ValueError:
        print("Invalid input. Please enter integers only.")

def is_prime():
    # This function checks if a given number is prime.
    try:
        num = int(input("Enter a number: "))
        if num <= 1:
            print(num, "is not a prime number.")
            return
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print(num, "is not a prime number.")
                return
        print(num, "is a prime number.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def factorial():
    # This function calculates the factorial of a number using a loop.
    try:
        n = int(input("Enter a number: "))
        if n < 0:
            print("Factorial is not defined for negative numbers.")
            return
        result = 1
        for i in range(2, n + 1):
            result *= i
        print(f"Factorial of {n} is {result}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def fibonacci_series():
    # This function prints the Fibonacci series up to n terms.
    try:
        n = int(input("Enter number of terms: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        a, b = 0, 1
        print("Fibonacci series:", end=" ")
        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()
    except ValueError:
        print("Invalid input. Please enter an integer.")

def reverse_number():
    # This function reverses a given integer number.
    try:
        num = int(input("Enter a number: "))
        rev = 0
        temp = abs(num)
        while temp > 0:
            rev = rev * 10 + temp % 10
            temp //= 10
        if num < 0:
            rev = -rev
        print(f"Reversed number: {rev}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Part B

# Student data structure using dictionary (no self/objects)
def create_student(name, roll_no, marks):
    # Returns a dictionary representing a student
    return {'name': name, 'roll_no': roll_no, 'marks': marks}

def display_student(student):
    print(f"Name: {student['name']}, Roll No: {student['roll_no']}, Marks: {student['marks']}")

def student_details():
    # This function creates a student (without using self) and displays the details.
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    try:
        marks = float(input("Enter marks: "))
    except ValueError:
        print("Invalid marks. Please enter a number.")
        return
    student = create_student(name, roll_no, marks)
    display_student(student)

def sort_array():
    # This function sorts an array of integers in ascending order.
    try:
        arr = list(map(int, input("Enter integers separated by space: ").split()))
        arr.sort()
        print("Sorted array:", arr)
    except ValueError:
        print("Invalid input. Please enter integers only.")

def is_palindrome():
    # This function checks if a string is a palindrome.
    s = input("Enter a string: ")
    if s == s[::-1]:
        print(f'"{s}" is a palindrome.')
    else:
        print(f'"{s}" is not a palindrome.')

def char_frequency():
    # This function counts the frequency of each character in a string.
    s = input("Enter a string: ")
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    print("Character frequencies:")
    for k, v in freq.items():
        print(f"{k}: {v}")

def remove_duplicates():
    # This function removes duplicate elements from a list of integers.
    try:
        arr = list(map(int, input("Enter integers separated by space: ").split()))
        unique = []
        seen = set()
        for num in arr:
            if num not in seen:
                unique.append(num)
                seen.add(num)
        print("Array after removing duplicates:", unique)
    except ValueError:
        print("Invalid input. Please enter integers only.")

def main_menu():
    # Main menu to select Part A or Part B questions
    while True:
        print("\nMain Menu:")
        print("1. Part A")
        print("2. Part B")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print("\nPart A:")
            print("1. Sum of two numbers")
            print("2. Check if a number is prime")
            print("3. Factorial using loop")
            print("4. Fibonacci series up to n terms")
            print("5. Reverse a number")
            sub = input("Enter your choice: ")
            if sub == '1':
                sum_of_two_numbers()
            elif sub == '2':
                is_prime()
            elif sub == '3':
                factorial()
            elif sub == '4':
                fibonacci_series()
            elif sub == '5':
                reverse_number()
            else:
                print("Invalid choice.")
        elif choice == '2':
            print("\nPart B:")
            print("1. Student class and display details")
            print("2. Sort array of integers")
            print("3. Check if string is palindrome")
            print("4. Character frequency in string")
            print("5. Remove duplicates from array")
            sub = input("Enter your choice: ")
            if sub == '1':
                student_details()
            elif sub == '2':
                sort_array()
            elif sub == '3':
                is_palindrome()
            elif sub == '4':
                char_frequency()
            elif sub == '5':
                remove_duplicates()
            else:
                print("Invalid choice.")
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
