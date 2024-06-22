
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__, template_folder='templates')
CORS(app)

# MongoDB connection
MONGO_URI = 'mongodb+srv://challakrish:Krishnaveni@cluster0.xqhlz9j.mongodb.net/'
client = MongoClient(MONGO_URI)
db = client['survey_new']
collection = db['responses']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/create', methods=['POST'])
def create_user():
    try:
        user = request.json
        result = collection.insert_one(user)
        return jsonify({'inserted_id': str(result.inserted_id)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/read', methods=['GET'])
def read_users():
    try:
        users = list(collection.find())
        for user in users:
            user['_id'] = str(user['_id'])
        return jsonify(users)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5500)




