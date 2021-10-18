from app.error_handler.error_handler import InvalidUsage
import app.error_handler.error_message as error_message
from typing import Dict, NoReturn

correct_values = {
    "Sex":  ["female", "male"],
    "Pclass" : [1, 2, 3]
}

correct_types = {
    "Name": str,
    "Sex": str,
    "Pclass": int,
    "Fare": float
}

def validate_length(payload: Dict) -> bool:
    return len(set([len(item) for key, item in payload.items()])) == 1

def validate_attributes(payload: Dict, attr: str) -> bool:
    validation = set([item in correct_values[attr] for item in payload[attr]])
    return len(validation) == 1 and list(validation)[0] == True

def validate_type(payload: Dict, attr: str) -> bool:
    validation = set([type(item) == correct_types[attr] for item in payload[attr]])
    return len(validation) == 1 and list(validation)[0] == True

def validate_payload(payload: Dict) -> NoReturn:
    if not validate_length(payload):
        raise InvalidUsage(error_message.get_messages(f"incorrect_length"))
    for key, value in correct_types.items():
        if not validate_type(payload, key):
            raise InvalidUsage(error_message.get_messages(f"incorrect_type_{key.lower()}"))
        if key in correct_values.keys() and not validate_attributes(payload, key):
            raise InvalidUsage(error_message.get_messages(f"incorrect_{key.lower()}"))

