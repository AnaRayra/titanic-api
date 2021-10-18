from typing import Dict

def get_messages(type_error: str) -> Dict:
   errors = {
    "incorrect_length": {"name": "Missing values.", "description":  "You need to enter all information for everyone."},
    "incorrect_sex": {"name": "Wrong value.", "description":  "Allowed values for the Sex field are: male/female"},
    "incorrect_pclass": {"name": "Wrong value.", "description":  "Allowed values for the Pclass field are: 1/2/3"},
    "incorrect_type_sex": {"name": "Wrong type.", "description": "Allowed type for the Sex field is String. Example: male"},
    "incorrect_type_pclass": {"name": "Wrong type.", "description": "Allowed type for the Pclass field is Integer. Example: 1"},
    "incorrect_type_fare": {"name": "Wrong type.", "description": "Allowed type for the Fare field is Float. Example: 50.0"},
  }
   return errors[type_error]