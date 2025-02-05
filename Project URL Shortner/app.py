from flask import Flask, request, redirect, render_template_string
import random
import string

app = Flask(__name__)

# In-memory storage for URLs
url_mapping = {}

# Function to generate a random short URL
def generate_short_url(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_url = generate_short_url()
        url_mapping[short_url] = long_url
        return f'Short URL is: <a href="/{short_url}">/{short_url}</a>'
    return '''<form method="post">
                Long URL: <input type="text" name="long_url">
                <input type="submit" value="Shorten">
               </form>'''

@app.route('/<short_url>')
def redirect_to_url(short_url):
    long_url = url_mapping.get(short_url)
    if long_url:
        return redirect(long_url)
    return "URL not found!"

if __name__ == '__main__':
    app.run(debug=True)
