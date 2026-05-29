SIMPLIFY_PROMPT = """
Rewrite the following literary passage into clear and natural modern English.

Rules:
- Preserve the original meaning exactly
- Preserve emotions, atmosphere, and narrative tone
- Use modern, readable English
- Avoid archaic or overly formal wording
- Avoid slang, internet language, or overly casual phrasing
- Do NOT summarize or shorten the passage
- Keep names unchanged
- Keep dialogue natural
- Maintain the emotional and literary beauty of the writing
- Make the passage easier for students and modern readers to understand

The rewritten version should feel elegant, emotionally faithful, and accessible.

Text:
"""



VOCAB_PROMPT = """
Identify only genuinely difficult, archaic, literary, or uncommon words from this passage.

Return ONLY in this exact format:

word : simple meaning

Rules:
- Do NOT explain common everyday words
- Ignore words understandable to average modern readers
- Include only words that may confuse students or non-native readers
- Meanings must use very simple English
- Keep explanations short and clear
- Maximum 5 words unless absolutely necessary

Text:
"""