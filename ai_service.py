import os
from openai import OpenAI
from textblob import TextBlob
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarise(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Summarise this call transcript briefly."},
            {"role": "user", "content": text}
        ]
    )

    return response.choices[0].message.content

def sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity