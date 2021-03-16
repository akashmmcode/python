from flask import Flask
import psycopg2

app = Flask(__name__)
db = 'postgresql://akash:qwerty7019354342@localhost/postgres'
conn = psycopg2.connect(db)
cursor = conn.cursor()

@app.route('/admin')
def hello_name():
    return "<h1 style= 'color: turquoise'>hello admin</h1>"

@app.route('/guest/<guest>') 
def hello_guest(guest):
    return f'hello_guest {guest}'

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_name')) 
    else:
        return redirect(url_for('hello_guest', guest = name))     
 
if __name__ =="__main__":
    app.run(debug=True)

