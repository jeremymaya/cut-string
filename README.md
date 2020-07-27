# cut-string

Author: Kyungrae Kim

Deployed Endpoint:

----

## Prompt

Write a small web application in Python/Ruby/Node. The application only needs to do the following:

* Accept a POST request to the route “/test”, which accepts one argument “string_to_cut”
* Return a JSON object with the key “return_string” and a string containing every third letter from the original string.

----

## Example

If you POST

```json
{"string_to_cut": "hellothere"}
```

it will return:

```json
{"return_string": "ltr"}
```

----

## Approach

### Approach using Enumerate

First approach is to use enumaerate to access index of the input string and build a new string.

```Python
string = "hellothere"
s = ""

for i, letter in enumerate(string, start=1):
    if i % 3 == 0:
        s += letter

return s
```

Complexity Analysis

* Time Complexity: ```O(n)```. We need to iterate every characater from the string where n is the length of input string.
* Space Complexity: ```O(n)```. The new string will store  ```1/3 * n``` where ne is where n is the length of input string.

### Appraoch using Join

Since strings in Python are immutable, a new string needs to be created to solve the problem. This continual copying from the initial apporach can lead to significant inefficiencies in Python programs.

We can optimize the above approach using more idomatic methods from Python using ```s = "".join(list)```

```Python
string = "hellothere"

slist = input[2::3]
s = "".join(slist)
```

Complexity Analysis

* Time Complexity: ```O(k)```. ```k``` is either the value of a parameter or the number of elements in the parameter.
* Space Complexity: ```O(n)```. The new string will store  ```1/3 * n``` where ne is where n is the length of input string.

----

## Credits

* [Data Science Blog - REST API Development with Flask](https://www.datascienceblog.net/post/programming/flask-api-development/)
* [Python - PerformanceTips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)
* [Python - TimeComplexity](https://wiki.python.org/moin/TimeComplexity#list)
* [Python Central - How to Slice Lists/Arrays and Tuples in Python](https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/)
* [pythonise.com - Working with JSON data | Learning Flask Ep. 9](https://pythonise.com/series/learning-flask/working-with-json-in-flask)
* [pytest - Parametrizing fixtures and test functions](https://docs.pytest.org/en/latest/parametrize.html)
