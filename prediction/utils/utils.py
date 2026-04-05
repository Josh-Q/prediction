def preprocess(candles):
    directions = [
        "UP" if c["close"] > c["open"] else "DOWN"
        for c in candles
    ]

    return {
        "last_5_directions": directions[-5:],
        "momentum_score": directions.count("UP") - directions.count("DOWN"),
        "last_close": candles[-1]["close"]
    }