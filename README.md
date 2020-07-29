# cut-string

Author: Kyungrae Kim

Endpoint: <https://cut-string.herokuapp.com/test>

----

## Prompt

Write a small web application in Python/Ruby/Node. The application only needs to do the following:

* Accept a POST request to the route “/test”, which accepts one argument “string_to_cut”
* Return a JSON object with the key “return_string” and a string containing every third letter from the original string.

----

## Example

If you POST

```JSON
{"string_to_cut": "hellothere"}
```

it will return:

```JSON
{"return_string": "ltr"}
```

Note: To see expected behavior you can test against a current working example with the command:

```bash
curl -X POST https://cut-string.herokuapp.com/test --data '{"string_to_cut": "hellothere"}' -H 'Content-Type: application/json'
```

----

## Approach

### Approach using Enumerate

The first approach is to use enumerate to access the index of the input string and build a new string.

```Python
string = "hellothere"
s = ""

for i, letter in enumerate(string, start=1):
    if i % 3 == 0:
        s += letter
return s
```

Complexity Analysis

* Time Complexity: ```O(n)```. We need to iterate every character from the string where ```n``` is the length of the input string.
* Space Complexity: ```O(n)```. The new string will store  ```1/3 * n``` where ```n``` is the length of input string.

### Approach using Join

Since strings in Python are immutable, a new string needs to be created to solve the problem. This continual copying from the initial approach can lead to significant inefficiencies in Python programs.

We can optimize the above approach using ```s = "".join(list)```

```Python
string = "hellothere"

slist = input[2::3]
s = "".join(slist)
return s
```

Complexity Analysis

* Time Complexity: ```O(k)```. Where ```k``` is either the value of a parameter or the number of elements in the parameter.
* Space Complexity: ```O(n)```. The new string will take ```1/3 * n``` space where ```n``` is the length of input string.

----

## Getting Started

Clone this repository to your local machine:

```bash
git clone https://github.com/jeremymaya/cut-string.git
```

Install the dependencies:

```bash
python3 -m pip install requirements.txt
```

### Development Mode

Start the application in development mode with the following command:

```bash
FLASK_ENV=development flask run
```

Test the functionality of the endpoint running at ```localhost:5000``` with the following command:

```bash
curl -X POST http://127.0.0.1:5000/test --data '{"string_to_cut": "hellothere"}' -H 'Content-Type: application/json'
```

The expected output of the above command is:

```JSON
{
    "return_string": "ltr"
}
```

Run the automated test with the following command:

```bash
pytest
```

The expected output of the above command is:

```bash
test/test_endpoints.py .............                                     [100%]

============================== 13 passed in 0.56s ==============================
```

### Production

Run the application in production with the following command:

```bash
uwsgi --ini app.ini --need-app
```

The application is currently deployed on Heroku with the following endpoint: <https://cut-string.herokuapp.com/test>

Run the automated test on the deployed Heroku with the following command:

```bash
pytest --host https://cut-string.herokuapp.com
```

----

## Credits

* [Data Science Blog - REST API Development with Flask](https://www.datascienceblog.net/post/programming/flask-api-development/)
* [Python - PerformanceTips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)
* [Python - TimeComplexity](https://wiki.python.org/moin/TimeComplexity#list)
* [Python Central - How to Slice Lists/Arrays and Tuples in Python](https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/)
* [pythonise.com - Working with JSON data | Learning Flask Ep. 9](https://pythonise.com/series/learning-flask/working-with-json-in-flask)
* [pytest - Parametrizing fixtures and test functions](https://docs.pytest.org/en/latest/parametrize.html)
* [uWSGI - Running python webapps on Heroku with uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/heroku_python.html)
* [Heroku Dev Center - Deploying Python Applications with Gunicorn](https://devcenter.heroku.com/articles/python-gunicorn)

----

## Change Log

* */test v1 deployment to Heroku Completed* - 27 Jul 2020
