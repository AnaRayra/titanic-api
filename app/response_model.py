import json
def get(name: str, pclass: int, sex: str, fare: float, decision: int) -> str:
    return json.dumps({
        "{name}": {
            "Informations": {
                "PClass": "{pclass}",
                "Sex": "{sex}",
                "Fare": "{fare}"
            },
            "Do this person has probability to survived the Titanic shipwreck?": "{decision}"
        }
    }).replace("{name}", str(name))\
        .replace("{pclass}", str(pclass))\
        .replace("{sex}", sex)\
        .replace("{fare}", str(fare))\
        .replace("{decision}", "Unfortunately, No" if decision == 1 else "Happily, Sim")