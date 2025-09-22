import argparse  # Imports the argparse module for parsing command-line arguments.
from app import chat_bot  # Imports the chat_bot object from the app module (contains chat_with_gpt).

def main():
    # Entry point for the CLI chatbot application.

    # Create an ArgumentParser instance.
    parser = argparse.ArgumentParser(
        prog="ChatBot",  # 'prog' sets the program name in help messages.
        description="A command-line chatbot using OpenAI API."  # 'description' shows in help output.
    )

    # Add a positional argument 'prompt' to the parser.
    parser.add_argument(
        "prompt",  # Name of the argument (user's message to the chatbot).
        type=str,  # Expects a string input.
        nargs="?",  # '?' means this argument is optional (can be omitted).
        help="Message to send to the chatbot (if omitted, enters interactive mode)"  # Help text for this argument.
    )

    # Parse the command-line arguments and store them in 'args'.
    args = parser.parse_args()

    # Check if the 'prompt' argument was provided by the user.
    if args.prompt:
        # Single message mode: user provided a prompt.
        # Call chat_with_gpt with the user's prompt and store the response.
        response = chat_bot.chat_with_gpt(args.prompt)
        # Print the chatbot's response to the terminal.
        print("AI:", response)
    else:
        # Interactive mode: no prompt provided, start a chat loop.
        print("ChatBot (type 'exit' or 'quit' to leave):")
        while True:
            # Prompt the user for input.
            user_input = input("You: ")
            # Convert input to lowercase and check for exit commands.
            if user_input.lower() in ("quit", "exit"):
                print("Goodbye!")  # Print exit message.
                break  # Exit the loop and end the program.
            # Send the user's input to the chatbot and get a response.
            response = chat_bot.chat_with_gpt(user_input)
            # Print the chatbot's response.
            print("AI:", response)

# This block ensures main() runs only if this file is executed directly.
if __name__ == "__main__":
    main()  # Call the main function to start the CLI chatbot.

# --- Flow Explanation ---
# 1. The script starts by importing necessary modules.
# 2. The main() function is defined and called if the script is run directly.
# 3. Inside main(), an ArgumentParser is created to handle CLI arguments.
# 4. The 'prompt' argument is added, which is optional.
# 5. Arguments are parsed from the command line.
# 6. If the user provides a prompt, the chatbot responds once and exits.
# 7. If no prompt is given, the chatbot enters interactive mode, repeatedly accepting user input and responding until the user types 'exit' or 'quit'.
# 8. All user inputs are sent to chat_with_gpt, which interacts with the OpenAI API and returns the AI's response.