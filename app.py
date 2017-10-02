
from flask import Flask
from flask_mysqldb import MySQL
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'bassel99'
app.config['MYSQL_DB'] = 'studentsbook'
app.config['MYSQL_HOST'] = '35.195.195.114'
mysql.init_app(app)
 
@app.route("/")
def hello():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM entries''')
    rv = cur.fetchall()
    return str(rv)
if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000')

