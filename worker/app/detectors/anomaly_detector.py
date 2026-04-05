import numpy as np # type: ignore
from sklearn.ensemble import IsolationForest  # type: ignore

# Intialize model globally
model = IsolationForest(contamination=0.1, random_state=42)

# Dummay training data (simulate normal behavior)
# Features: [response_time, log_level_encoded]

training_data = np.array([
    [0.2, 0],
    [0.5, 0],
    [1.0, 1],
    [0.3, 0],
    [0.7, 1],
    [0.4, 0],
])

model.fit(training_data)


# feature engineering
def encoded_level(level:str) -> int:
    mapping = {
        "INFO": 0,
        "WARNING": 1,
        "ERROR": 2
    }

    return mapping.get(level, 0)

def extract_features(log: dict):
    """
    Convert log into numerical feture
    """
    return [
        log.get("response_time", 0),
        encoded_level(log.get("level", "INFO"))
    ]

def is_anomaly(log: dict) -> bool:
    features = extract_features(log)

    prediction = model.predict([features])

    return bool(prediction[0] == -1)

