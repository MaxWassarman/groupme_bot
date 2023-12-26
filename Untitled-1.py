import requests
import json
import datetime

def read_message_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().strip()

def send_groupme_message(bot_id, text):
    url = "https://api.groupme.com/v3/bots/post"
    
    payload = {
        "bot_id": bot_id,
        "text": text
    }
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 202:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message. Status Code: {response.status_code}. Response: {response.text}")

if __name__ == "__main__":
    BOT_ID = 'dbc8a405a8e385c629638de26b'

    # Manually define file paths for each day
    day_to_file_path = {
        'Tuesday': '/Users/maxwassarman/Desktop/groupme_bot/Tuesday.txt'
    }

    # Get current day of the week
    current_day = datetime.datetime.today().strftime('%A')

    # Use the current day to get the corresponding file path
    message_file_path = day_to_file_path.get(current_day, 'default.txt')
    
    message_text = read_message_from_file(message_file_path)
    send_groupme_message(BOT_ID, message_text)
