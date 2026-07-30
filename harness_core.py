
import re
from typing import Dict, Any

class ParamValidator:
    def __init__(self, param_schema: Dict[str, Any]):
        self.schema = param_schema

    def validate(self, params: Dict[str, Any]) -> bool:
        for key, value in self.schema.items():
            if key not in params:
                return False
            if value.get("type") == "int":
                if not re.match("^[0-9]+$", str(params[key])):
                    return False
            elif value.get("type") == "float":
                if not re.match("^[0-9]+(\.[0-9]+)?$", str(params[key])):
                    return False
            elif value.get("type") == "str":
                if not isinstance(params[key], str):
                    return False
            elif value.get("type") == "bool":
                if not isinstance(params[key], bool):
                    return False
        return True


class HarnessCore:
    def __init__(self, param_schema: Dict[str, Any]):
        self.validator = ParamValidator(param_schema)

    def execute(self, params: Dict[str, Any]) -> bool:
        if self.validator.validate(params):
            # Execute core logic
            return True
        return False


class HarnessAPI:
    def __init__(self, core: HarnessCore):
        self.core = core

    def execute(self, params: Dict[str, Any]) -> bool:
        return self.core.execute(params)


class HarnessServer:
    def __init__(self, api: HarnessAPI):
        self.api = api

    def handle_request(self, params: Dict[str, Any]) -> bool:
        return self.api.execute(params)


class HarnessClient:
    def __init__(self, server: HarnessServer):
        self.server = server

    def send_request(self, params: Dict[str, Any]) -> bool:
        return self.server.handle_request(params)


# Example usage:
if __name__ == "__main__":
    param_schema = {
        "int_param": {"type": "int"},
        "float_param": {"type": "float"},
        "str_param": {"type": "str"},
        "bool_param": {"type": "bool"}
    }
    core = HarnessCore(param_schema)
    api = HarnessAPI(core)
    server = HarnessServer(api)
    client = HarnessClient(server)
    
    params = {
        "int_param": 123,
        "float_param": 123.45,
        "str_param": "hello",
        "bool_param": True
    }
    result = client.send_request(params)
    print(result)
