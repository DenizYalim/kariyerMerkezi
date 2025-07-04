from flask import Flask, request, jsonify
from llm import getResponse

app = Flask(__name__)

# print(getResponse("hello gpt what's 5+5"))

@app.route("/getResponse", methods=["GET"])
def get_recipeList():
    message = request.args.get("message")
    context = request.args.get("context")
    
    if not message:
        return jsonify({"error": "Missing 'message' parameter"}), 400

    response = getResponse(message, context)


    return jsonify({"response": response})

@app.route('/ping', methods=['GET'])
def ping():
    
    return jsonify({"message":"pong"}), 200

@app.route('/test_llm', methods=['GET', 'POST'])
def test_llm():
    
    test_message = request.args.get("message")
    context = "You are able to talk"

    if not test_message:
        test_message = "Hello gpt, how are you doing. what's 5+5?"
    response = getResponse(test_message, context)

    return jsonify({"response": response}), 200

if __name__ == "__main__":
    app.run(port=5002, debug = True)
