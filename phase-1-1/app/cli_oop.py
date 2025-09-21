import argparse
import sys  # Import the argparse module for command-line argument parsing
from app import calculator_oop as cls  # Import calculator class from another file    

def main():
    parser = argparse.ArgumentParser(
        prog="Calculator",  # Name of the program   
        description="A command-line calculator application.",  # Short description
    )

    subparsers = parser.add_subparsers(dest="cmd", required=True, help="Available operations")

    add_parser = subparsers.add_parser("add", help="Add two numbers")
    add_parser.add_argument("a", type=float, help="First number")  # First
    add_parser.add_argument("b", type=float, help="Second number")  # Second number argument

    subtract_parser = subparsers.add_parser("subtract", help="Subtract two numbers")
    subtract_parser.add_argument("a", type=float, help="First number")  # First number argument
    subtract_parser.add_argument("b", type=float, help="Second number")  # Second number argument

    multiply_parser = subparsers.add_parser("multiply", help="Multiply two numbers")
    multiply_parser.add_argument("a", type=float, help="First number")  # First
    multiply_parser.add_argument("b", type=float, help="Second number")  # Second number argument

    divide_parser = subparsers.add_parser("divide", help="Divide two numbers")
    divide_parser.add_argument("a", type=float, help="First number")  # First
    divide_parser.add_argument("b", type=float, help="Second number")  # Second

    args = parser.parse_args()

    calculator = cls.Calculator()  # Create an instance of the Calculator class

    try:
        if args.cmd == "add":
            result = calculator.add(args.a, args.b)  # Call add method
        elif args.cmd == "subtract":
            result = calculator.subtract(args.a, args.b)  # Call subtract method
        elif args.cmd == "multiply":
            result = calculator.multiply(args.a, args.b)  # Call multiply method
        elif args.cmd == "divide":
            result = calculator.divide(args.a, args.b)  # Call divide method
        else:
            print("Unknown command.")  # Handle unknown command
            return
    except ZeroDivisionError as e:
        print(e)  # Print error if division by zero occurs
        return  
    print(f"Result: {result}")  # Print the result of the calculation


if __name__ == "__main__":
    main()  # Run the main function if this file is executed directly