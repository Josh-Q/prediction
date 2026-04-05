
from ollama_ai.prompt import build_prompt, clean_llm_response
from utils.utils import preprocess    
from ollama_ai.client import call_model
import json

if __name__ == "__main__":

    # candles = fetch_candles()
    # indicators = map_indicators()
    candles = [
        {"open": 100, "close": 104},
        {"open": 104, "close": 103},
        {"open": 103, "close": 106},
        {"open": 106, "close": 108},
        {"open": 108, "close": 107}
    ]

    indicators = {
        "MA5": 106,
        "MA20": 102,
        "RSI": 64,
        "MACD": 0.5,
        "Trend": "UPTREND"
    }

    features = preprocess(candles)
    prompt = build_prompt(features, indicators)
    result = call_model(prompt)
    result = clean_llm_response(result)

    # Example trading logic
    if float(result["confidence"]) > 0.6:
        print("TRADE:", result["prediction"])
    else:
        print("NO TRADE (low confidence)")
