import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
(os.getenv("OPENAI_API_KEY"))
client = openai.OpenAI()

def getResponse(prompt,  context = None):
    if context is None:
        context = "If the user asks to make a new flight, call endpoint /addFlight"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

# print(getResponse("Hello gpt how are you doing? what is 1 + 1"))


if __name__ != "__main__": 
    pass