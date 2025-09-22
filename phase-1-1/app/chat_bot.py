import requests
import os
from dotenv import load_dotenv

load_dotenv()

def chat_with_gpt(prompt):
    api_key = os.getenv("OPENAI_KEY")
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code}, {response.text}"
    
# def main():
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ("quit", "exit"):
#             print("Goodbye!")
#             break
#         response = chat_with_gpt(user_input)
#         print("AI:", response)

# if __name__ == "__main__":
#     main()
