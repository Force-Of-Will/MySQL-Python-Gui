#imports
import tkinter as tk
import mysql.connector
from mysql.connector.errors import Error
import time
#make the root for the GUI
root=tk.Tk()
root.title("Player Play Game Database GUI")
# setting the GUIs size
root.geometry("600x400")
  
# declaring string variable
# for storing name and password
query_var=tk.StringVar()
 
# defining a function that will
# get the name and password and
# print them in the terminal screen
def submit():
    start_time = time.time()
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "project1"
    )
    mycursor = mydb.cursor()
    
    query=query_var.get()
     
    print("The query is : \"" + query +"\"")
    try:
        mycursor.execute(query);
        myresult = mycursor.fetchall();
        for x in myresult:
            print(x); 
    except mysql.connector.Error as err:
        print("Error Querying Data. Try Again. Error: {}".format(err))
    query_var.set("")
    print("My program took", time.time() - start_time, "to run")
#       -End SUBMIT()-      #

#       -Delete_Players-        #
def delete_players():
    start_time = time.time()
    print("Called Delete Players")
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "project1"
    )
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM PLAYERS");
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
    #except: print("Error deleting records from Players.") 
    print("My program took", time.time() - start_time, "to run")
#       -End Delete_Players()-      #

#       -Delete_Play-        #
def delete_play():
    start_time = time.time()
    print("Called Delete Play")
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "project1"
    )
    mycursor = mydb.cursor()
    try:
        mycursor.execute("DELETE FROM PLAY");
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
    except:
        print("Error deleting records from Play.")    
    print("My program took", time.time() - start_time, "to run")
#       -End Delete_Play()-      #

#       -Delete_Games-        #
def delete_game():
    start_time = time.time()
    print("Called Delete Games")
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "project1"
    )
    mycursor = mydb.cursor()
    try:
        mycursor.execute("DELETE FROM GAMES");
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
    except:
        print("Error deleting records from Games.")  
    print("My program took", time.time() - start_time, "to run")
#       -End Delete_Players()-      #

#       -DEBUG-     #
def debug():
    print("Setting debug values!")
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "project1"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO players VALUES(%s, %s, %s, %s, %s, %s, %s)"
    val = [
        ("bob", "1", "aggies", "QB", "42", "80", "15000"),
        ("John", "2", "Texas Tech", "RB", "1", "12", "12000"),
        ("Alice", "3", "Texas Tech", "WR", "2", "15", "13500"),
        ("Sam", "4", "Aggies", "RB", "0", "5", "5000"),
        ("Ben", "5", "Losers", "QB", "100", "4242", "50000")    
    ]#end val
    try:
        mycursor.executemany(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) inserted into Players.");
    except:
        print("Error: make sure none of your records are duplicates!");
    
    sql = "INSERT INTO games VALUES(%s, %s, %s, %s, %s, %s)"
    val = [
        ("1", "2020/01/01", "aggie stadium", "W", "1000", "45000"),
        ("2", "2020/01/02", "Texas Tech Stadium", "L", "450", "1500"),
        ("3", "2020/01/03", "Texas Tech Stadium", "T", "12", "0"),
        ("4", "2020/01/04", "Aggie Stadium", "L", "15000", "100000"),
        ("5", "2020/01/05", "Bens Backyard", "T", "0", "0")    
    ]#end val
    try:
        mycursor.executemany(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) inserted into Games.");
    except:
        print("Error: make sure none of your records are duplicates!");
        
    sql = "INSERT INTO play VALUES(%s, %s)"
    val = [
        ("1", "5"),
        ("2", "4"),
        ("3", "3"),
        ("4", "2"),
        ("5", "1")
    ]#end val
    try:
        mycursor.executemany(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) inserted into Play.");
    except:
        print("Error: make sure none of your records are duplicates!");
     
def readPlayers():
    start_time = time.time()
    f = open("Players.txt", "r")
    myList = []
    for x in f:
        myArr = x.replace("\n", "").split(",")
        #print(myArr)
        myArr = tuple(myArr)
        myList.append(myArr)
    f.close()
    #print(myList)
    sql = "INSERT INTO players VALUES(%s, %s, %s, %s, %s, %s, %s)"
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "project1"
    )
    mycursor = mydb.cursor()
    count = 0
    for x in myList:
        try:
            mycursor.execute(sql, x)
            count = count + 1;
        except mysql.connector.Error as err:
            print("Could not insert data into Players: {}".format(err) + str(x))
    mydb.commit()
    print(str(count) + " record(s) inserted into Players.");
    print("My program took", time.time() - start_time, "to run")
    
def readPlay():
    start_time = time.time()
    f = open("Play.txt", "r")
    myList = []
    for x in f:
        myArr = x.replace("\n", "").split(",")
        #print(myArr)
        myArr = tuple(myArr)
        myList.append(myArr)
    f.close()
    #print(myList)
    sql = "INSERT INTO play VALUES(%s, %s)"
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "project1"
    )
    mycursor = mydb.cursor()
    count = 0
    for x in myList:
        try:
            mycursor.execute(sql, x)
            count = count + 1;
        except mysql.connector.Error as err:
            print("Could not insert data into Play: {}".format(err) + str(x))
    mydb.commit()
    print(str(count) + " record(s) inserted into Play.");
    print("My program took", time.time() - start_time, "to run")
    
def readGame():
    start_time = time.time()
    f = open("Game.txt", "r")
    myList = []
    for x in f:
        myArr = x.replace("\n", "").split(",")
        #print(myArr)
        myArr = tuple(myArr)
        myList.append(myArr)
    f.close()
    #print(myList)
    sql = "INSERT INTO games VALUES(%s, %s, %s, %s, %s, %s)"
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "project1"
    )
    mycursor = mydb.cursor()
    count = 0
    for x in myList:
        try:
            mycursor.execute(sql, x)
            count = count + 1;
        except mysql.connector.Error as err:
            print("Could not insert data into Game: {}".format(err) + str(x))
    mydb.commit()
    print(str(count) + " record(s) inserted into Games.");
    print("My program took", time.time() - start_time, "to run") 
     
def bulkPlayers():
    start_time = time.time()
    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "project1"
        )
        mycursor = mydb.cursor()
        sql = "load data infile 'C:/Users/blong/Desktop/Phase2/Players.txt' into table players fields terminated by ',' lines terminated by '\\n';"
        mycursor.execute(sql)
    except mysql.connector.Error as err:
        print("Something went horribly wrong: {}".format(err))
    mydb.commit()
    print("My program took", time.time() - start_time, "to run")
    
def bulkPlay():
    start_time = time.time()
    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "project1"
        )
        mycursor = mydb.cursor()
        sql = "load data infile 'C:/Users/blong/Desktop/Phase2/Play.txt' into table play fields terminated by ',' lines terminated by '\\n';"
        mycursor.execute(sql)
    except mysql.connector.Error as err:
        print("Something went horribly wrong: {}".format(err))
    mydb.commit()
    print("My program took", time.time() - start_time, "to run")
    
def bulkGame():
    start_time = time.time()
    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "project1"
        )
        mycursor = mydb.cursor()
        sql = "load data infile 'C:/Users/blong/Desktop/Phase2/Game.txt' into table games fields terminated by ',' lines terminated by '\\n';"
        mycursor.execute(sql)
    except mysql.connector.Error as err:
        print("Something went horribly wrong: {}".format(err))
    mydb.commit()
    print("My program took", time.time() - start_time, "to run")
     
# creating a label for
# query using widget Label
query_label = tk.Label(root, text = 'Query', font=('calibre',10, 'bold'))
  
# creating a entry for input
# query using widget Entry
query_entry = tk.Entry(root,textvariable = query_var, font=('calibre',10,'normal'), width = 65)
  
# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit Query', command = submit)

#creating a label for deletions
del_label = tk.Label(root, text = 'Delete', font=('calibre',10, 'bold'))
#creating a button using button widget that will delete the data from all tables
del_btn_players=tk.Button(root,text = 'DELETE ALL PLAYERS', command = delete_players)
del_btn_play=tk.Button(root,text = 'DELETE ALL PLAY', command = delete_play)
del_btn_game=tk.Button(root,text = 'DELETE ALL GAME', command = delete_game)
dbg_btn = tk.Button(root, text = "DEBUG", font=('calibre',10, 'bold'), command = debug)

#creating label for Insertions
insert_label = tk.Label(root, text = 'Single Insert', font=('calibre',10, 'bold'))
#creating buttons for Insertions
insert_playerstxt=tk.Button(root,text = 'Insert from Players.txt', command = readPlayers)
insert_playtxt=tk.Button(root,text = 'Insert from Play.txt', command = readPlay)
insert_gametxt=tk.Button(root,text = 'Insert from Game.txt', command = readGame)
  
#creating label for Insertions
bulk_label = tk.Label(root, text = 'Bulk Insert', font=('calibre',10, 'bold'))
#creating buttons for Insertions
bulk_playerstxt=tk.Button(root,text = 'Insert from Players.txt', command = bulkPlayers)
bulk_playtxt=tk.Button(root,text = 'Insert from Play.txt', command = bulkPlay)
bulk_gametxt=tk.Button(root,text = 'Insert from Game.txt', command = bulkGame)  
  
# placing the label and entry in the required position using grid method
query_label.grid(row=0,column=0)
query_entry.grid(row=0,column=1)
sub_btn.grid(row=0,column=2)
dbg_btn.grid(row=1, column = 0)
del_label.grid(row=1, column = 1)
del_btn_players.grid(row=4, column = 1)
del_btn_play.grid(row=2, column = 1)
del_btn_game.grid(row=3, column = 1)

insert_label.grid(row=5, column=1)
insert_playerstxt.grid(row=6, column = 1)
insert_gametxt.grid(row=7, column = 1)
insert_playtxt.grid(row=8, column = 1)

bulk_label.grid(row = 9, column = 1)
bulk_playerstxt.grid(row = 10, column = 1)
bulk_playtxt.grid(row = 12, column = 1)
bulk_gametxt.grid(row = 11, column = 1)
  
# performing an infinite loop
# for the window to display
root.mainloop() #this line copy pasted from w3schools' GUI tutorial
