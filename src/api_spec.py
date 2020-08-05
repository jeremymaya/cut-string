from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import Schema, fields

spec = APISpec(
    title="Cut String",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

class InputSchema(Schema):
    string_to_cut = fields.String(description="A string to be processed", required=True)

class OutputSchema(Schema):
    return_string = fields.String(description="A string containing every third letter from the original string")

class ErrorSchema(Schema):
    message = fields.String(description="An error message")

spec.components.schema("Input", schema=InputSchema)
spec.components.schema("Output", schema=OutputSchema)

tags = [
            {"name": "cut string",
             "description": "Funtion for processing a string"
            },
       ]

for tag in tags:
    print(f"Adding tag: {tag['name']}")
    spec.tag(tag)