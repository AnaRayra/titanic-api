from typing import Dict, List
import app.model as model
import app.response_model as response_model
import app.validation as validation
import json

def mock_payload(infos: Dict, response: List) -> Dict:
    payload_final = {}
    persons_quantity = len(infos["Pclass"])
    i = 1
    while i <= persons_quantity:
        payload_final.update(
            json.loads(response_model.get(infos["Name"][i - 1],
                                          infos["Pclass"][i - 1],
                                          infos["Sex"][i - 1],
                                          infos["Fare"][i - 1],
                                          response[i - 1]
                                          )
                       )
        )
        i += 1
    return payload_final


def transforms_payload(payload: List) -> Dict:
    transformed_payload = {
        "Name": [],
        "Pclass": [],
        "Sex": [],
        "Fare": []
    }

    for row in payload:
        for key in transformed_payload.keys():
            transformed_payload[key].append(row[key])

    return transformed_payload


def people_prediction(payload: List) -> Dict:
    payload = transforms_payload(payload)
    validation.validate_payload(payload)
    response = model.run_model(payload)
    return mock_payload(payload, response)