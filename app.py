from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jokes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Joke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content
        }

@app.route('/joke', methods=['GET'])
def get_joke():
    jokes = Joke.query.all()
    if not jokes:
        return jsonify({'message': 'No jokes found'}), 404
    joke = random.choice(jokes)
    return jsonify(joke.to_dict())

@app.route('/joke', methods=['POST'])
def add_joke():
    data = request.json
    new_joke = data.get('joke')
    if not new_joke:
        return jsonify({'error': 'No joke provided'}), 400
    joke = Joke(content=new_joke)
    db.session.add(joke)
    db.session.commit()
    return jsonify(joke.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)