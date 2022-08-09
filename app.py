from flask import Flask,render_template,request,flash,redirect

from dbm import addPlayer, deletePlayerById, getAllPlayers, getPlayerById, updatePlayerById
from model import Cricket2K

app=Flask(__name__)

@app.route('/',methods=['get'])
def index():
    n='Cricket2K21'
    return render_template('index.html',username=n)

@app.route('/login',methods=['get'])
def l():
    return "<h2>Unavailable</h2>"

@app.route('/getplayers',methods=['get'])
def showplayers():
    data=getAllPlayers()
    return render_template('players.html',players=data)
  
@app.route('/addplayer')
def showAddPlayerForm():
    return render_template('addplayer.html')


@app.route('/saveplayer',methods=['post'])
def saveplayer():
    name=request.form['player']
    role=request.form['role']
    rating=request.form['rating']
    rating_num=int(rating)
    pid=request.form['id']
    pid_num=int(pid)
    player=Cricket2K(name,role,rating_num,pid_num)
    addPlayer(player)
    return redirect('/getplayers')

@app.route('/deleteplayer/<int:i>')
def deleteplayer(i):
    deletePlayerById(i)
    return redirect('/getplayers')

@app.route('/getplayer/<int:i>')
def getplayer(i):
    g=getPlayerById(i)
    return render_template('updateplayer.html',player=g)

@app.route('/updateplayer',methods=['post'])
def updateplayer():
    i=request.form['pid']
    pid=int(i)
    name=request.form['player']
    role=request.form['role']
    r=request.form['rating']
    rating=int(r)
    c=Cricket2K(name,role,rating,pid)
    updatePlayerById(c)
    return redirect('/getplayers')

if __name__=='__main__':
    app.run(debug=True)

