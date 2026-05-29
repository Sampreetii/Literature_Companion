import os
import google.generativeai as genai
from dotenv import load_dotenv
from prompts import SIMPLIFY_PROMPT, VOCAB_PROMPT

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def simplify_text(text):
    response = model.generate_content(
        SIMPLIFY_PROMPT + text
    )
    return response.text


def explain_words(text):
    response = model.generate_content(
        VOCAB_PROMPT + text
    )
    return response.text