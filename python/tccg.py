import openai

# Set your API key
api_key = 'YOUR_API_KEY'

def ask_gpt3(question):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # Free tier uses text-davinci-002 engine
        prompt=question,
        max_tokens=50  # Adjust the max tokens as needed
    )
    return response.choices[0].text

try:
    # Your code that might raise an exception
    
except Exception as e:
    # If an exception occurs, query ChatGPT for help
    question = f"Python error: {str(e)}. How can I fix it?"
    response = ask_gpt3(question)
    print("ChatGPT Response:")
    print(response)
