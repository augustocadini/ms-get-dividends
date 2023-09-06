import os
import json

from flask import Flask, jsonify, request

from app.src.model.dividends_get_request import DividendsGetRequest
from app.src.impl.dividends_impl import read_dividends
from werkzeug.exceptions import HTTPException

# Init Flask
app = Flask(__name__)


# ==== Endpoints Definition ==== #


@app.route('/healthcheck', methods=['GET'])
def health_check():
    print('Healthcheck')
    return jsonify({'status': 'ok'})


@app.route('/v1/stock/dividends', methods=['POST'])
def v1_get_dividends():
    print('V1 Get Dividends')
    api_key = request.headers.get('X-API-Key')
    print(f"Payload: {json.dumps(request.json)}")
    dividend_request = DividendsGetRequest(**request.json)
    result = read_dividends(api_key, dividend_request)
    return jsonify(result)


# Custom error handler function
@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps(e.description)
    response.content_type = "application/json"
    return response

# ==== Main Function ==== #


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
