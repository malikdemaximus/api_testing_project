# utils/schema_validator.py

import jsonschema
import json

def validate_schema(response_json, schema_path):
    with open(schema_path) as f:
        schema = json.load(f)
    jsonschema.validate(instance=response_json, schema=schema)
