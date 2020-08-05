import os
import pytest
import requests
from openapi_spec_validator import validate_spec_url

@pytest.mark.parametrize(
    "payload,expected",
    [
        ({"string_to_cut": "hellothere"}, "ltr"),
        ({"string_to_cut": "iam"}, "m"),
        ({"string_to_cut": "ia"}, ""),
        ({"string_to_cut": "i"}, ""),
        ({"string_to_cut": ""}, ""),
        ({"string_to_cut": "123"}, "3"),
        ({"string_to_cut": "!@#"}, "#"),
        ({"string_to_cut": "   "}, " ")
    ],
)
def test_cut_string_expected(host, payload, expected):
    endpoint = os.path.join(host, 'test')
    response = requests.post(endpoint, json=payload)
    assert response.status_code == 200
    json = response.json()
    assert 'return_string' in json
    assert json['return_string'] == expected

@pytest.mark.parametrize(
    "payload",
    [
        ({"string_to": "hellothere"}),
        ({"string": "hellothere"}),
        ({"": "hellothere"}),
        ({}),
        (),
    ],
)
def test_cut_string_exception(host, payload):
    endpoint = os.path.join(host, 'test')
    response = requests.post(endpoint, json=payload)
    assert response.status_code == 400
    json = response.json()
    assert 'message' in json
    assert json['message'] == 'Request body must be a JSON object with the key “string_to_cut” and a string'

def test_swagger_specification(host):
    endpoint = os.path.join(host, 'api', 'swagger.json')
    validate_spec_url(endpoint)