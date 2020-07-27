# cut-string

Author: Kyungrae Kim

Deployed Endpoint:

## Prompt

Write a small web application in Python/Ruby/Node. The application only needs to do the following:

* Accept a POST request to the route “/test”, which accepts one argument “string_to_cut”
* Return a JSON object with the key “return_string” and a string containing every third letter from the original string.

## Example

If you POST

```json
{"string_to_cut": "hellothere"}
```

it will return:

```json
{"return_string": "ltr"}
```

## Approach

## Credits
