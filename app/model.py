import pandas as pd
import joblib
from typing import Dict, List

model = joblib.load("./app/model_training/model.pkl")

def run_model(payload: Dict) -> List:
    data = pd.DataFrame(payload, columns=['Pclass', 'Sex', 'Fare'])
    result = model.predict(data)
    return result.tolist()
