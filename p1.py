import mysql.connector

con = mysql.connector.connect(
    user = "root",
    host = "127.0.0.1",
    database = "sravanth_1"
    
    
)

cursor = con.cursor()

word=input("Enter the word: ")

query = cursor.execute("SELECT * FROM user_details WHERE first_name = '%s'" % word)
results = cursor.fetchall()

if results:
    print(result[0])
else:
    print("No word found!")
