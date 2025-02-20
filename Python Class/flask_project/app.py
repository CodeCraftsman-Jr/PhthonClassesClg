from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class CSKTeam(Resource):
    team = []

    def get(self):
        return jsonify({"team": self.team})

    def post(self):
        data = request.json
        if data:
            self.team.append(data)
            return jsonify({"team": self.team})
        return jsonify({"message": "No data received"})

api.add_resource(CSKTeam, '/csk')

@app.route('/')
def home():
    return "Welcome to Flask!"

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

@app.route('/vasanth')
def vasanth():
    return "Route node arrived"

@app.route('/hell/<vasanth>')
def hell(vasanth):
    return f"Welcome home, {vasanth}!"

@app.route('/csk', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        data = request.json
        return {"message": "Data received", "data": data}
    return {"message": "Send a POST request with JSON data"}

if __name__ == '__main__':
    app.run(debug=True)