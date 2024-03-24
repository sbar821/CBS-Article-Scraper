import openai
import os

openai_api_key=os.getenv('OPENAI_API_KEY')

def get_summary(filename):
    with open(filename, 'r') as file:
        sanitized = file.read()

    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Write the article title then summarize this article in 50 words or less: {sanitized}"}
        ],
        temperature = 0,
        max_tokens=100
    )

    return completion.choices[0].message.content
