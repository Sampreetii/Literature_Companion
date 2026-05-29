import os
import re
import json

import google.generativeai as genai

from dotenv import load_dotenv
from prompts import MASTER_PROMPT


load_dotenv()


API_KEY = os.getenv(
    "GEMINI_API_KEY"
)


if not API_KEY:

    raise Exception(
        "Missing GEMINI_API_KEY"
    )


genai.configure(
    api_key=API_KEY
)


model = genai.GenerativeModel(
    "gemini-2.5-flash",
    generation_config={
        "temperature":0.4
    }
)



def extract_json(text):

    text = (
        text.replace("```json","")
        .replace("```","")
        .strip()
    )


    match = re.search(
        r"\{.*\}",
        text,
        re.DOTALL
    )


    if not match:

        raise Exception(
            "Invalid AI response"
        )


    return json.loads(
        match.group()
    )




def process_text(text, level):


    instruction=f"""

Reading Mode:

{level}


Simple:
Very clear beginner-friendly English.

Modern:
Natural English for today's readers.

Literary:
Keep more poetic style but remove outdated language.

"""


    prompt=f"""

{MASTER_PROMPT}


{instruction}


{text[:15000]}

"""


    response=model.generate_content(
        prompt
    )


    return extract_json(
        response.text
    )