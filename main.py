from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send_message():
    number = request.json['number']
    message = request.json['message']
    url = f"https://api.whatsapp.com/send?phone={number}&text={message}"
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    app.run(port=5000)

