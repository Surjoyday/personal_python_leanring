import argparse  # Import the argparse module for command-line argument parsing
from app import calculator_function as fnc  # Import calculator functions from another file

def main():
    # Create the main argument parser for the CLI app
    parser = argparse.ArgumentParser(
        prog="Calculator",  # Name of the program
        description="A command-line calculator application.",  # Short description
    )

    # Create subparsers for different calculator operations (add, subtract, etc.)
    subparsers = parser.add_subparsers(dest="cmd", required=True, help="Available operations")

    # Add subparser for the 'add' command
    add_parser = subparsers.add_parser("add", help="Add two numbers")
    add_parser.add_argument("a", type=float, help="First number")  # First number argument
    add_parser.add_argument("b", type=float, help="Second number")  # Second number argument

    # Add subparser for the 'subtract' command
    subtract_parser = subparsers.add_parser("subtract", help="Subtract two numbers")
    subtract_parser.add_argument("a", type=float, help="First number")  # First number argument
    subtract_parser.add_argument("b", type=float, help="Second number")  # Second number argument

    # Add subparser for the 'multiply' command
    multiply_parser = subparsers.add_parser("multiply", help="Multiply two numbers")
    multiply_parser.add_argument("a", type=float, help="First number")  # First number argument
    multiply_parser.add_argument("b", type=float, help="Second number")  # Second number argument

    # Add subparser for the 'divide' command
    divide_parser = subparsers.add_parser("divide", help="Divide two numbers")
    divide_parser.add_argument("a", type=float, help="First number")  # First number argument
    divide_parser.add_argument("b", type=float, help="Second number")  # Second number argument

    # Parse the command-line arguments entered by the user
    args = parser.parse_args()

    try:
        # Check which operation was chosen and call the corresponding function
        if args.cmd == "add":
            result = fnc.add(args.a, args.b)  # Call add function
        elif args.cmd == "subtract":
            result = fnc.subtract(args.a, args.b)  # Call subtract function
        elif args.cmd == "multiply":
            result = fnc.multiply(args.a, args.b)  # Call multiply function
        elif args.cmd == "divide":
            result = fnc.divide(args.a, args.b)  # Call divide function
        else:
            print("Unknown command.")  # Handle unknown command
            return
    except ValueError as e:
        print(e)  # Print error if division by zero occurs
        return

    print(f"Result: {result}")  # Print the result of the calculation

if __name__ == "__main__":
    main()  # Run the main function if this file is executed directly



#========================================================================================
# WHAT IS ARGPARSE AND WHY DO WE USE IT?
#========================================================================================

# WHAT IS ARGPARSE?
# - argparse is Python's built-in library for creating command-line interfaces (CLI)
# - It automatically handles parsing command-line arguments that users provide
# - It generates help messages, handles errors, and validates input
# - Think of it as a "smart translator" between what users type and what your program needs

# WHY USE ARGPARSE INSTEAD OF SIMPLE INPUT() OR TERMINAL I/O?
# Let's compare the two approaches:

# METHOD 1: Using simple input() (the basic way)
# -----------------------------------------------
# def simple_calculator():
#     print("Welcome to calculator!")
#     operation = input("Enter operation (add/subtract/multiply/divide): ")
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     # ... do calculation
#
# Problems with this approach:
# 1. INTERACTIVE ONLY: User must manually type each input every time
# 2. NO AUTOMATION: Can't be used in scripts or batch processing
# 3. NO VALIDATION: No automatic error checking for invalid inputs
# 4. NO HELP: Users don't know what options are available
# 5. SLOW: Takes multiple steps for each calculation

# METHOD 2: Using argparse (the professional way)
# ------------------------------------------------
# What we have in this file - users can run:
# python -m app.cli_func add 5 3
#
# Advantages of argparse:
# 1. ONE COMMAND: Everything in a single line
# 2. SCRIPTABLE: Can be easily used in shell scripts and automation
# 3. BATCH PROCESSING: Can process multiple calculations quickly
# 4. AUTOMATIC HELP: Users can run --help to see all options
# 5. INPUT VALIDATION: Automatically checks if arguments are valid
# 6. PROFESSIONAL: Standard way to build CLI tools (like git, docker, etc.)

# REAL-WORLD COMPARISON:
# ----------------------
# Simple input() approach:
# $ python calculator.py
# > Welcome to calculator!
# > Enter operation: add
# > Enter first number: 5
# > Enter second number: 3
# > Result: 8
# (4 interactions needed, can't automate)

# argparse approach:
# $ python -m app.cli_func add 5 3
# > Result: 8
# (1 command, can be automated, can be scripted)

# AUTOMATION EXAMPLES:
# -------------------
# With argparse, you can do things like:
# 
# 1. Batch calculations:
# for i in {1..10}; do python -m app.cli_func add $i 5; done
#
# 2. Use in shell scripts:
# result=$(python -m app.cli_func multiply 4 6)
# echo "The answer is: $result"
#
# 3. Pipe with other commands:
# echo "Numbers: 10, 20" | xargs python -m app.cli_func add
#
# You CAN'T do these things with simple input() because it requires human interaction!

# PROFESSIONAL TOOLS USE ARGPARSE:
# --------------------------------
# Examples of tools that work like our argparse calculator:
# - git add filename.txt (not: "git" -> "what do you want?" -> "add" -> "what file?")
# - docker run image-name (not interactive prompts)
# - pip install package-name (not step-by-step questions)
# - ls -la (not "ls" -> "what options?" -> "-la")

# ARGPARSE FEATURES WE GET FOR FREE:
# ----------------------------------
# 1. Help messages: python -m app.cli_func --help
# 2. Error handling: python -m app.cli_func add (missing arguments)
# 3. Type conversion: Automatically converts "5" string to 5.0 float
# 4. Subcommands: Different operations (add, subtract, etc.) in one program
# 5. Argument validation: Ensures required arguments are provided

# WHEN TO USE EACH APPROACH:
# --------------------------
# Use input() when:
# - Building interactive applications (games, questionnaires)
# - You want to guide users step-by-step
# - Building educational/learning tools where interaction helps understanding
#
# Use argparse when:
# - Building command-line tools for developers/power users
# - Creating utilities that need to be automated or scripted
# - Building professional software that others will use in their workflows
# - You want your tool to behave like standard Unix/Linux commands

# SUMMARY:
# --------
# argparse makes your Python programs behave like professional command-line tools.
# It's the difference between a toy calculator and a tool that can be used in 
# real workflows, automation, and professional development environments.

