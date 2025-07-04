from flask import Flask, request, Response, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

JOB_API_URL = "http://localhost:5001"
GPT_URL = "http://localhost:5002"

def proxy_request(target_url):
    method = request.method
    headers = {key: value for key, value in request.headers if key != 'Host'}
    data = request.get_data()
    params = request.args

    resp = requests.request(method, target_url, headers=headers, params=params, data=data)
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]

    return Response(resp.content, resp.status_code, headers)

@app.route("/ping", methods = ["GET", "POST", "PATCH", "DELETE"])
def ping_gateway():
    message =  "pinged python api gateway"
    return Response(message, 200, mimetype='text/plain')

@app.route("/job/<path:path>", methods = ["GET", "POST", "PATCH", "DELETE"])
def llm_proxy(path):
    actual_path = f"{JOB_API_URL}/{path}"
    return proxy_request(actual_path)

@app.route("/gpt_api/<path:path>", methods = ["GET", "POST", "PATCH", "DELETE"])
def spring_proxy(path):
    actual_path = f"{GPT_URL}/{path}"
    return proxy_request(actual_path)

if __name__ == "__main__":
    app.run(port=5000, debug = True) # Note: don't forget to turn off debug later on
