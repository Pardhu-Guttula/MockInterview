from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error
import config

app = Flask(__name__)

@app.route('/interview-slots/available', methods=['GET'])
def get_data():
    connection = connect_to_db(config.MYSQL_DB)
    # print(connection)
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            query = "SELECT * FROM interviewfact where interviewStatus = 'Pending'"
            cursor.execute(query)
            data = cursor.fetchall()

            if data:
                return jsonify(data)
            else:
                return jsonify("Invalid Credentials")
        except Error as e:
            return jsonify({'error': str(e)})
    else:
        return jsonify({'error':"Connection failed"})


def connect_to_db(db):
    try:
        connection = mysql.connector.connect(
            host = config.MYSQL_HOST,
            user = config.MYSQL_USER,
            password = config.MYSQL_PASSWORD,
            database = db
        )
        if connection:
            print("Connected to", db, "database")
            # print(connection)
            return connection
            
    except Error as e:
        print("Error in connecting to", e )
        return None

if __name__=="__main__":
    app.run(debug=True)