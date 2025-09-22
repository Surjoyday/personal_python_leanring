import argparse
from app import chat_bot

def main():
    parser = argparse.ArgumentParser(
        prog="ChatBot",
        description="A command-line chatbot using OpenAI API."
    )
    parser.add_argument(
        "prompt",
        type=str,
        nargs="?",
        help="Message to send to the chatbot (if omitted, enters interactive mode)"
    )

    args = parser.parse_args()

    if args.prompt:
        # Single message mode
        response = chat_bot.chat_with_gpt(args.prompt)
        print("AI:", response)
    else:
        # Interactive mode
        print("ChatBot (type 'exit' or 'quit' to leave):")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ("quit", "exit"):
                print("Goodbye!")
                break
            response = chat_bot.chat_with_gpt(user_input)
            print("AI:", response)

if __name__ == "__main__":
    main()
