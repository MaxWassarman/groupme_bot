from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

def send_groupme_message(bot_id, text):
    url = "https://api.groupme.com/v3/bots/post"
    payload = {
        "bot_id": bot_id,
        "text": text
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.status_code

@app.route('/get_info', methods=['GET'])
def get_info():
    with open("info.json", "r") as f:
        data = json.load(f)
    return jsonify(data), 200

@app.route('/update_info', methods=['POST'])
def update_info():
    new_info = request.json
    with open("info.json", "w") as f:
        json.dump(new_info, f)
    return jsonify({"message": "Info updated successfully"}), 200

@app.route('/send_message', methods=['POST'])
def send_message():
    BOT_ID = 'dbc8a405a8e385c629638de26b'
    
    with open("info.json", "r") as f:
        data = json.load(f)
        
    # Construct your message based on the info in data
    message = "Some message based on info"
    
    status_code = send_groupme_message(BOT_ID, message)
    
    if status_code == 202:
        return jsonify({"message": "Message sent successfully"}), 200
    else:
        return jsonify({"message": "Failed to send message"}), 400

if __name__ == '__main__':
    app.run(debug=True)
