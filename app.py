from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your details
ENDPOINT = "https://pranay-joshi-task6.cognitiveservices.azure.com/"
PROJECT_NAME = "Pranay-Joshi-Task6C-Health-Care-FAQs"
DEPLOYMENT_NAME = "production"
API_KEY = "AK2B2XNLvmAXzKJ1QDhGLlevhwlgineymyxkw6Z1WYeR6i17kkNyJQQJ99BDACYeBjFXJ3w3AAAaACOGBPAq"

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.json.get("question", "")
    
    headers = {
        "Ocp-Apim-Subscription-Key": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "question": user_question,
        "top": 1
    }

    response = requests.post(
        f"{ENDPOINT}/language/:query-knowledgebases?projectName={PROJECT_NAME}&deploymentName={DEPLOYMENT_NAME}&api-version=2021-10-01",
        headers=headers,
        json=payload
    )

    result = response.json()
    answer = result["answers"][0]["answer"] if result["answers"] else "Sorry, I don’t know the answer."

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

