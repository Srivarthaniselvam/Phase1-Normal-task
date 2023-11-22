# Phase 1
# Normal Task

import string
import random

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
        return result if not result.is_integer() else int(result)
    except ZeroDivisionError:
        return "Error: Division by zero"

def get_user_input():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Please enter valid numbers.")

def select_operation():
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            return choice
        else:
            print("Invalid input. Please enter a valid choice (1/2/3/4).")

def calculator():
    print("Welcome to My Simple Calculator")

    while True:
        num1, num2 = get_user_input()
        operator = select_operation()

        operations = {
            '1': add,
            '2': subtract,
            '3': multiply,
            '4': divide
        }

        try:
            result = operations[operator](num1, num2)
            operator_symbol = {'1': '+', '2': '-', '3': '*', '4': '/'}[operator]
            print(f"\nResult: {num1} {operator_symbol} {num2} = {result}")
        except Exception as e:
            print(f"Error: {e}")

        exit_choice = input("Do you want to perform another operation? (y/n): ")
        if exit_choice.lower() != 'y':
            print("Thank you for using My Calculator!")
            break


calculator()
