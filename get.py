from flask import Flask
import psycopg2

app = Flask(__name__)
db = 'postgresql://akash:qwerty7019354342@localhost/postgres'
conn = psycopg2.connect(db)
cur = conn.cursor()

@app.route('/')
def connectdb():
    cur.execute("select * from categories")
    conn.commit()
    categories = cur.fetchall()
    result_str = 'ID     Category\n- - - - - - - -\n'
    
    x = [(id, category), (id, category)]
    for i in categories:
        result_str = result_str + f'{i[0]}     {i[1]}\n'
    
    return result_str



if __name__ =="__main__":
    app.run(debug=True)