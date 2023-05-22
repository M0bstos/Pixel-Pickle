from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

api_key = os.environ.get('OPENAI_API_KEY')

api_url = "https://api.openai.com/v1/images/generations"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']

        payload = {
            "prompt": prompt,
            "n": 4,
            "size": "512x512"
        }

        response = requests.post(api_url, json=payload, headers=headers)

        if response.status_code == 200:
            result = response.json()
            images = result["data"]
            return render_template('result.html', images=images)
        else:
            error_message = f"Error: {response.text}"
            return render_template('error.html', error_message=error_message)

    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
