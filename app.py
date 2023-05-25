from flask import Flask,render_template,flash, redirect,url_for,json,request
from mysql.connector import connect

app = Flask(__name__)

con = connect(host='mssql-128238-0.cloudclusters.net',port=18013,database='asign',user='root',password='Bhanusri@3626')
cur = con.cursor(buffered=True)

cur.execute('create table val(name varchar(255))')
cur.execute('insert into val values(%s)',('test',))
con.commit()

@app.route('/')
def home():
    cur.execute('select * from val')
    d = cur.fetchone()
    print(d)
    return d[0]

@app.route('/admin')
def admin():
    cur.execute('select * from val')
    data = cur.fetchall()
    return render_template('admin.html',data=data)

@app.route('/adminchange',methods=['GET','POST'])
def change():
    if request.method=='POST':
        d = request.form['name']
        cur.execute('update val set name=%s',(d,))
        con.commit()
        return redirect('/')
    else:
        return 'get'

if __name__=='__main__':
    app.run(debug=True)

