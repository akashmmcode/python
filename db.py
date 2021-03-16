import psycopg2

con = psycopg2.connect(database = "postgres", 
                        user= "akash", 
                        password = "qwerty7019354342", 
                        host = "localhost",
                        port = 5432)

cur = con.cursor()

# # cur.execute("INSERT INTO categories(category_id,category_name)VALUES(%s,%s)",(5,"cabrolite"))
cur.execute("SELECT * FROM categories") 
# con.commit()   

rows = cur.fetchall()
print(rows)

cur.close()
con.close()