from email import message
import imp
import json
import jsonschema

from rest_framework import serializers

flow_tmpl_rule = {
    "type": "array",
    "items": {
        "type": "object",
        "properties":{
            "name":{
                "type": "string",
            },
            "description": {
                "type": "string"
            },
            "component_code": {
                "type": "string",
            },
            "version": {
                "type": "string",
            },
            "inputs": {
                "type": "array",
                "items": {
                    "type":"object",
                    "properties": {
                        "key": {
                            "type": "string"
                        },
                        "value": {
                            "type": "string"
                        }
                    },
                    "required": ["key", "value"]
                }
            }
        },
        "required": ["name", "description", "component_code", "version", "inputs"]
    }
}


class FlowTmplTreeValidtor():
    def __call__(self, value):
        try:
            jsonschema.validate(value, flow_tmpl_rule)
        except jsonschema.ValidationError as e:
            message = str(e)
            raise serializers.ValidationError(message)
