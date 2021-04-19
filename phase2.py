import mysql.connector
print("Successfully imported connector.")

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Nmsuaggies1",
    database = "project1"
    )

print(mydb)

mycursor = mydb.cursor()

#       -Create a DB-     #
#try:
#    mycursor.execute("CREATE DATABASE helloWorld");
#except:
#    print("Could not create database");

#       -Create a Table-        #
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))");

#       -See if a DB exists you are looking for-        #
#mycursor.execute("SHOW DATABASES");
#for x in mycursor: print(x)
#       -See if a Table exists you are looking for-         #
#mycursor.execute("SHOW TABLES");
#for x in mycursor: print(x)

#kind of a single insert
#sql = "INSERT INTO players VALUES(%s, %s, %s, %s, %s, %s, %s)"
#val = ("bob", "1", "aggies", "QB", "42", "80", "15000")
#try:
#    mycursor.execute(sql, val)
#    mydb.commit()
#    print(mycursor.rowcount, "record(s) inserted.")
#except:
#    print("Error inserting data. Make sure data does not already exist! (not a duplicate!)")


#       -Larger insertions-     #
#sql = "INSERT INTO players VALUES(%s, %s, %s, %s, %s, %s, %s)"
#val = [
#    ("bob", "2", "aggies", "QB", "42", "400", "15000"),
#    ("alice", "3", "lobos", "WR", "0", "12", "0"),
#    ("cheif", "4", "aggies", "RB", "12", "15", "1200"),
#    ("ben", "5", "panthers", "QB", "100", "20", "10000"),
#    ("jane", "1", "aggies", "WR", "4", "800", "2400")    
#    ]#end val
#try:
#    mycursor.executemany(sql, val)
#    mydb.commit()
#    print(mycursor.rowcount, "record(s) inserted");
#except:
#    print("Error: make sure none of your records are duplicates!");

mycursor.execute("SELECT * FROM players where name = 'jane'");
myresult = mycursor.fetchall();
for x in myresult:
    print(x);
