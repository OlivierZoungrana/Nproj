from flask import Flask, jsonify
from flask_restful import Api

from connection import connection, cursor

app = Flask(__name__)
api = Api(app)


class getcrud():
    @app.route('/test', methods=['GET'])
    def get():
        cursor.execute("select * from rest_api.test")
        rows= cursor.fetchall()
        connection.close()
        return jsonify({"Testdetails": rows})

if __name__ == '__main__':
    app.run(debug=True)