import json
import re


def build_prompt(features, indicators):
    return f"""
You are a high-frequency quantitative trading model.

Your task is to predict the NEXT candle direction.

Output STRICT JSON ONLY:
{{
  "prediction": "POSITIVE or NEGATIVE",
  "confidence": 0-1
}}

DO NOT include explanations.

---

Features:
{json.dumps(features)}

Indicators:
{json.dumps(indicators)}

---

Rules:
- Use momentum, trend, and indicator confluence
- If signals conflict, reduce confidence
- If unclear, choose best probability but keep confidence low

Output must be valid JSON only.
"""


def clean_llm_response(raw_text):
    """
    Remove code fences, markdown, whitespace, and extract JSON.
    """
    # Remove triple backticks and optional language hints
    raw_text = re.sub(r"```[a-zA-Z]*\n?", "", raw_text)
    raw_text = raw_text.replace("```", "")
    raw_text = raw_text.strip()

    # Extract JSON block safely
    match = re.search(r"\{.*\}", raw_text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except Exception as e:
            print("JSON parsing error:", e)

    # Fallback
    return {"prediction": "NEGATIVE", "confidence": 0.0}