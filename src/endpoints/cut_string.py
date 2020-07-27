from flask import Blueprint
from flask import jsonify
from flask import request

cut_string = Blueprint(name='cut_string', import_name=__name__)


@cut_string.route('/test', methods=['POST'])
def test():
    """
    ---
    post:
      description: Returns a string containing every third letter from the original string
      requestBody:
        required: true
        content:
            application/json:
                schema: InputSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: OutputSchema
        '400':
          description: call fail
          content:
            application/json:
              schema: OutputSchema
      tags:
          - cut string
    """
    try:
        data = request.json
        string = data['string_to_cut']
        slist = string[2::3]
        s = "".join(slist)
        output  = {"return_string": s}
        return jsonify(output)
    except:
        output  = {"message": "Request body must be a JSON object with the key “string_to_cut” and a string"}
        return jsonify(output), 400