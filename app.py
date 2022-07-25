from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql
app=Flask(__name__)
@app.route("/")
@app.route("/index")
def index():
    con=sql.connect("database.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from students")
    data=cur.fetchall()
    return render_template("index.html",datas=data)
@app.route("/add_student",methods=['POST','GET'])
def add_student():
    if request.method=='POST':
        name=request.form['name']
        grade=request.form['grade']
        con=sql.connect("database.db")
        cur=con.cursor()
        cur.execute("insert into students(name,grade) values (?,?)",(name,grade))
        con.commit()
        flash('Name and Grade Added','success')
        SID+=1
        return redirect(url_for("index"))

    return render_template("add_student.html")

@app.route("/edit_student/str(SID)",methods=['POST','GET'])
def edit_student(SID):
    if request.method=='POST':
        name=request.form['name']
        grade=request.form['grade']
        con=sql.connect("database.db")
        cur=con.cursor()
        cur.execute("update students set NAME=?,GRADE=? where SID=?",(name,grade,SID))
        con.commit()
        flash('Student Updated','success')
        return redirect(url_for("index"))
    con=sql.connect("database.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from students where SID=?",(SID,))
    data=cur.fetchone()
    return render_template("edit_student.html",datas=data)

@app.route("/delete_student/str(SID)",methods=['GET'])
def delete_student(SID):
    con=sql.connect("database.db")
    cur=con.cursor()
    cur.execute("delete from students where SID=?",(SID,))
    con.commit()
    flash('Student Deleted','warning')
    return redirect(url_for("index"))

if __name__=='__main__':
    app.secret_key='yihong'
    app.run(debug=True)
##Reference from https://www.youtube.com/watch?v=xIkAEe0Rb8Q
##But the content has been improved and updated to the hw material.
##
