from typing import Dict

class InvalidUsage(Exception):

    def __init__(self, message: Dict):
        Exception.__init__(self)
        self.message = message
        self.status_code = 400

    def to_dict(self) -> Dict:
        rv = dict()
        rv['Description'] = self.message["description"]
        rv['Error'] = self.message["name"]
        return rv