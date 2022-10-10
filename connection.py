import os
from dotenv import load_dotenv
from flask import Flask
import mysql.connector
load_dotenv()
app = Flask(__name__)
connection = mysql.connector.connect(host='localhost', database=os.getenv('DATABASE'), user='root', password=os.getenv('PASSWORD'), auth_plugin='mysql_native_password')
cursor = connection.cursor()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

