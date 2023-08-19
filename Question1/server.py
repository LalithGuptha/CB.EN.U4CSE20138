from flask import Flask, jsonify
from datetime import datetime, timedelta
import requests

app = Flask(__name__)

u1="http://20.244.56.144/train/auth"

body={
    "companyName": "Lalith Railways",
    "clientID": "a29d8644-4780-46d5-ba63-9be999f9341d",
    "ownerName": "Lalith Guptha B",
    "ownerEmail": "blalithguptha@gmail.com",
    "rollNo": "CB.EN.U4CSE138",
    "clientSecret": "ehnNZfARfsBVGBRa"
}
x = requests.post(u1, json=body)
btoken = x.json()['access_token']



API_URL = "http://20.244.56.144/train/trains"
BEARER_TOKEN = btok
@app.route('/trains', methods=['GET'])
def get_train_schedule():
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    response = requests.get(API_URL, headers=headers)

    if response.status_code == 200:
        trains = response.json()
    else:
        return jsonify({"error": f"Error fetching train data: {response.status_code}"}), 500

    now = datetime.now()
    twelve_hours_later = now + timedelta(hours=12)

    valid_trains = []

    for train in trains:
        departure_time = datetime(now.year, now.month, now.day,
                                  train['departureTime']['Hours'],
                                  train['departureTime']['Minutes'],
                                  train['departureTime']['Seconds']) + timedelta(minutes=train['delayedBy'])

        if now + timedelta(minutes=30) <= departure_time <= twelve_hours_later:
            valid_trains.append(train)

    sorted_trains = sorted(valid_trains, key=lambda x: ((x['price']['AC']+x['price']['sleeper']), -(x['seatsAvailable']['AC']+x['seatsAvailable']['sleeper']),
                                                        -x['departureTime']['Hours'] * 60 - x['departureTime']['Minutes'] + x['delayedBy']))

    return jsonify(sorted_trains)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
