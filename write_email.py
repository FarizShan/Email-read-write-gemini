import google.generativeai as genai

# Set your API key
genai.configure(api_key="Enter gemini api key")

# Define the system prompt and model
system_prompt = """
Please write an email in the style of the user given a prompt and the sample emails below. 
It should be formal, keep the email content within 50 words, 
just express what the user says in the prompt. Sign the email as Fariz.


My name is fariz, and my student number is chn21cs052. I'm 4th year CSE student in College of engineering chengannur.

"""

def create_email():
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Start the chat with the system prompt
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": system_prompt},
        ]
    )

    user_prompt = input("Describe the email you want. \n")
    
    while user_prompt.lower() != "done":
        # Send user input as a message
        response = chat.send_message(user_prompt)
        print("\nGenerated Email:\n")
        print(response.text)

        # Ask if the user wants to continue
        user_prompt = input("\nPlease type 'done' if satisfied; otherwise, continue describing your changes. \n")
    
    final_draft = response.text
    return final_draft

# Run the function
if __name__ == "__main__":
    final_email = create_email()
    print("\nFinal Draft:\n")
    print(final_email)
