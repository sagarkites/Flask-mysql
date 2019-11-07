from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/',methods = ['GET', 'POST'])
def home():
	if request.method == 'POST':
		userDetails = request.form
		email = userDetails['email']
		password = userDetails['password']
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO students(email,password) VALUES(%s,%s)",(email,password))
		mysql.connection.commit()
		cur.close()
		return redirect(url_for('welcome'))
	return render_template('login.html')

@app.route('/welcome')
def welcome():
	return render_template('get.html')

if __name__ == '__main__':
   app.run(debug=True)	
