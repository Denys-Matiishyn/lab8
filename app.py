import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="auction"
)

cursor = db.cursor(dictionary=True)


@app.route('/buyers', methods=['GET'])
def get_buyers():
    cursor.execute("SELECT * FROM buyers")
    return jsonify(cursor.fetchall())


@app.route('/buyers', methods=['POST'])
def add_buyer():
    data = request.get_json()

    sql = "INSERT INTO buyers (f_name, s_name, phone_number, email) VALUES (%s, %s, %s, %s)"
    values = (data['f_name'], data['s_name'], data['phone_number'], data['email'])

    cursor.execute(sql, values)
    db.commit()

    return jsonify({"message": "Buyer added"})


@app.route('/buyers/<int:id>', methods=['PUT'])
def update_buyer(id):
    data = request.get_json()

    sql = "UPDATE buyers SET f_name=%s, s_name=%s, phone_number=%s, email=%s WHERE id=%s"
    values = (data['f_name'], data['s_name'], data['phone_number'], data['email'], id)

    cursor.execute(sql, values)
    db.commit()

    return jsonify({"message": "Buyer updated"})


@app.route('/buyers/<int:id>', methods=['DELETE'])
def delete_buyer(id):
    cursor.execute("DELETE FROM buyers WHERE id=%s", (id,))
    db.commit()

    return jsonify({"message": "Buyer deleted"})


if __name__ == '__main__':
    app.run(debug=True)


    @app.route('/', methods=['GET'])
    def index():
        return jsonify({"message": "Hello, server is running!"})

