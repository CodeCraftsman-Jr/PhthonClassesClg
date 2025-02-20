from flask import Flask, request, redirect, render_template
import random
import string

app = Flask(__name__)

# In-memory storage for URLs
url_mapping = {}

# Function to generate a random short URL
def generate_short_url(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_url = generate_short_url()
        url_mapping[short_url] = long_url
    return render_template('index.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_url(short_url):
    long_url = url_mapping.get(short_url)
    if long_url:
        return redirect(long_url)
    return "URL not found!"

if __name__ == '__main__':
    app.run(debug=True)
