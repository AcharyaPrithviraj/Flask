import pymysql
from model import Cricket2K
def connect():
    global connection, cursor
    connection=pymysql.connect(host="localhost",user="root",password="",db="Cricket2k21")
    cursor=connection.cursor()
    

def disconnect():
    global connection, cursor
    cursor.close()
    connection.close()
    
def addPlayer(player):
    global cursor,connection
    connect()
    query='insert into Ptable(name,role,rating,id) values(%s,%s,%s,%s)'
    cursor.execute(query,(player.name,player.role,player.rating,player.pid))
    connection.commit()#save the data
    disconnect()
    print('done')

def getAllPlayers():
    global cursor,connection
    connect()
    query="select * from Ptable"
    cursor.execute(query)
    data=cursor.fetchall()
    disconnect()
    return data

def getPlayerById(pid):
    global cursor,connection
    connect()
    query="select * from Ptable where id=%s"
    cursor.execute(query,(pid))
    data=cursor.fetchone()
    disconnect()
    return data

def deletePlayerById(pid):
    global cursor,connection
    connect()
    query="delete from Ptable where id=%s"
    cursor.execute(query,(pid))
    connection.commit()
    disconnect()
    
def updatePlayerById(player):
    global cursor,connection
    connect()
    query="update ptable set name=%s,role=%s,rating=%s where id=%s"
    cursor.execute(query,(player.name,player.role,player.rating,player.pid))
    connection.commit()
    disconnect()
