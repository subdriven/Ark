<<<<<<< Updated upstream:app/app.py
from flask import Flask, render_template, json, request
#from flask.ext.mysql import MySQL
#from werkzeug import generate_password_hash, check_password_hash
import MySQLdb
app = Flask(__name__)
#mysql = MySQL()

# MySQL config
db = MySQLdb.connect(host="localhost", port=3306, user="ark2", passwd="ark2", db="ark2")
cursor = db.cursor()

#cursor.execute("SELECT * FROM BDR_MAST where ID=15")

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/<item>")
def main(item):
#  return render_template('index.html')
  cursor.execute("SELECT * FROM BDR_MAST where ID=%s", (item))
  result = cursor.fetchall()
#  return str(result)
  return render_template('show_results.html')

@app.route('/showSignUp')
def showSignUp():
  return render_template('signup.html')

@app.route('/signUp',methods=['POST'])
def signUp():
  #read posted data from UI
  _name = request.form['inputName']
  _email = request.form['inputEmail']
  _password = request.form['inputPassword']

# validate the received values
  if _name and _email and _password:
    return json.dumps({'html':'<span>All fields good !!</span>'})
  else:
    return json.dumps({'html':'<span>Enter the required fields</span>'})

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

