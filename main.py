from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'  # SQLite database file name

db = SQLAlchemy(app)

# Define the Person model
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f"{self.id}: {self.name}"

# Create the database tables (if they don't exist)
db.create_all()

@app.route('/')
def intro():
    return 'HNG Backend Stage 2 Task - Simple CRUD RESTful API'

# Create new person
@app.route('/people', methods=['POST'])
def add_person():
    name = request.json.get('name')
    if not name:
        return jsonify({"message": "Name is required"}), 400

    person = Person(name=name)
    db.session.add(person)
    db.session.commit()

    return jsonify({"message": f"'{name}' has been added successfully"}), 201

# Update name, get and delete single person by id
@app.route('/people/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def person(id):
    person = Person.query.get(id)
    if not person:
        return jsonify({"message": "Person not found"}), 404

    if request.method == 'GET':
        return jsonify({"id": person.id, "name": person.name})

    elif request.method == 'PUT':
        new_name = request.json.get('name')
        if not new_name:
            return jsonify({"message": "Name is required"}), 400

        person.name = new_name
        db.session.commit()
        return jsonify({"message": "Person updated successfully"})

    elif request.method == 'DELETE':
        db.session.delete(person)
        db.session.commit()
        return jsonify({"message": "Person deleted successfully"})

# Get names of all people on db
@app.route('/people/all', methods=['GET'])
def get_all_people():
    try:
        people = Person.query.all()
        people_list = [{"id": person.id, "name": person.name} for person in people]
        return jsonify(people_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run()
