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
        "GEMINI_API_KEY missing"
    )


genai.configure(
    api_key=API_KEY
)


model = genai.GenerativeModel(
    "gemini-2.5-flash",
    generation_config={
        "temperature": 0.4
    }
)


def extract_json(text):

    text = text.strip()

    text = (
        text.replace("```json", "")
            .replace("```", "")
    )

    match = re.search(
        r"\{.*\}",
        text,
        re.DOTALL
    )

    if not match:

        raise Exception(
            "AI returned invalid JSON"
        )

    return json.loads(
        match.group()
    )


def process_text(text, level):

    if level == "Simple":

        instruction = """

You are rewriting this passage for a reader aged 12–14.

Goals:
- Make the text very easy to understand
- Use short, clear sentences
- Replace difficult vocabulary
- Explain implied ideas naturally
- Preserve the meaning exactly
- Preserve emotions and important imagery

Rules:
- Do not summarize
- Do not remove details
- Use everyday English
- The result should feel like a modern young-adult novel

"""

    elif level == "Modern":

        instruction = """

You are rewriting this passage as if it were written today.

Goals:
- Preserve meaning exactly
- Preserve emotions and atmosphere
- Use natural contemporary English
- Remove archaic wording
- Improve readability

Rules:
- Do not summarize
- Do not simplify excessively
- Keep important imagery and descriptions
- The result should feel like a bestselling modern novel

"""

    else:

        instruction = """

You are adapting this passage into contemporary literary fiction.

This is NOT a simple rewrite.

Goals:
- Preserve all meaning and important details.
- Preserve the narrator's personality and emotions.
- Preserve atmosphere and symbolism.

You SHOULD:
- Restructure sentences when beneficial.
- Improve rhythm and flow.
- Rewrite awkward translated phrasing.
- Make the prose feel like a modern award-winning novel.

The result should feel freshly written,
not lightly edited.

Imagine this passage is being rewritten by a contemporary literary novelist.

Do not summarize.
Do not remove information.

"""

    prompt = f"""

{MASTER_PROMPT}

READING STYLE:

{instruction}

PASSAGE:

{text[:15000]}

"""

    response = model.generate_content(
        prompt
    )

    return extract_json(
        response.text
    )