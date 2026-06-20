import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def action(r):
    if r.lower()=="walk walk":
        return("ARF ARF ARF ARF ARF ARF ARF ARF ARF ARF ARF ARF")
    elif r.lower()=="greenie":
        return("woof woof woof woof woof woof woof woof woof")
    elif r.lower()=="no more greenies":
        return("grrrrrr grrrrrr grrrrrr grrrrrr grrrrrr grrrrrr")
    elif "chicken" in r.lower():
        return("A-WOOOOOOOOOOO")
    elif "no treats" in r.lower():
        return("hey not cool man")
    else:
        return response(r)

def response(r):
    result = _client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are Chive, a dog. Respond using only dog sounds like woof, arf, bork, ruff, grr, awoo, yip. No real English. No actions. Maximum 5 words."},
            {"role": "user", "content": r},
        ],
        temperature=0.9,
    )
    return result.choices[0].message.content.strip()
