from re import template
from flask import Flask, render_template,request,session,url_for,redirect
import random
import sqlite3
from datetime import date
from passlib.hash import sha256_crypt
from werkzeug.utils import redirect
app=Flask(__name__)
app.config["SECRET_KEY"]="235#2009"


quotes=['A reader lives a thousand lives before he dies.',
'A person who never reads lives only once.',
'never trust a person who has\'nt read a book',
'You Can find Magic wherever you LOOK. Sit back and Relax, all you Need is a BOOK',
'The more that you READ, the more things you will KNOW. The more that you LEARN, the more places you\'ll GO.',
'A book is a gift that can be opened again and again.',
'Reading gives us some place to go when we have to stay were we are.',
'Reading is dreaming with open eyes.',
'A child who reads will be an adult who thinks.',
'Reading is never a waste of time!',
]
leaderboard=['p1','p2','p3','p4','p5','p6']

quote=random.choice(quotes)    
             
# @app.route('/', methods=['GET', 'POST'])
# def password():
    # if request.method=="GET":
    #     return render_template("members_registration.html")
    # username=request.form.get("username")
    # session["username"]=username
    # if request.method=="GET":
    #     return render_template("password.html")
    # password=request.form.get("password")    
    # message="To access the website please enter the password!"
    # print(password)
    # if password=="Jr7+2m21":
    #     return render_template("index.html",quote=quote)
    # else:
    #     return render_template('password.html',error="incorrect password")
    

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html",quote=quote)

@app.route('/home', methods=['GET', 'POST'])
def home():
    conn=sqlite3.connect('database/readersclub.db')
    cur=conn.cursor()
    if request.method=="GET":
        return render_template("readersclubhomepage.html",leaderboard=leaderboard)
    feedback=request.form.get("feedback")
    name=request.form.get("user_name")    
    user_feedback={}    
    print(user_feedback)
    session["fb"]=feedback                                     
    session["un"]=name
    user_feedback[name]=feedback
    session["feedback"]=user_feedback 
    cur.execute('INSERT INTO feedback (name,feedback) VALUES(?,?);',[name,feedback])
    conn.commit()
    conn.close()
    return render_template("readersclubhomepage.html",message="feedback sent succesfully",leaderboard=leaderboard)
    
   
@app.route('/library', methods=['GET', 'POST'])
def library():
    return render_template("access_library.html")

@app.route('/quizz', methods=['GET', 'POST'])
def quizz():
    return render_template("quizz.html")


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    return render_template("feedback.html")

user_suggested=[]    
@app.route('/good_books', methods=['GET', 'POST'])
def good_books():
    good_books=request.form.get("good_books")

    
    print(user_suggested)
    
    user_suggested.append(good_books)
    session["good_books"]=user_suggested
    
    print(user_suggested)              
    return render_template("readersclubhomepage.html",books=user_suggested,leaderboard=leaderboard)

@app.route('/register', methods=['GET', 'POST'])
def register():
    conn=sqlite3.connect('database/readersclub.db')
    cur=conn.cursor()
    if request.method=="POST":
        name=request.form.get("name")
        username=request.form.get("username")
        age=request.form.get("age")
        email=request.form.get("email")
        password=request.form.get("password")
        password=sha256_crypt.encrypt(password)
        message=''
        confirm_password=request.form.get('confirm_password')
        cur.execute('SELECT username FROM members_registration where username=?;',[username])
        user_record=cur.fetchone()
        if user_record!=None:
            eroor='username already exists'
            return render_template('members_registration.html',error=eroor)
        if sha256_crypt.verify(confirm_password,password) ==False:
            message='password mismatch try again'
            return render_template('members_registration.html',message=message)
        gender=request.form.get("gender")
        cur.execute('INSERT INTO members_registration(name,username,age,email,password,gender) \
                    VALUES (?,?,?,?,?,?);',[name,username,age,email,password,gender])
        conn.commit()
        print('values inserted')
        conn.close()
    return render_template('members_registration.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error=""
    conn=sqlite3.connect("database/readersclub.db")
    cur=conn.cursor()
    if request.method=="POST":
        role=request.form.get("role")
        print(role)
        username=request.form.get("username")
        print(username)
        password=request.form.get("password")
        print(password)
        cur.execute("Select username, password from members_registration where username=?;",[username])
        records=cur.fetchone()
        print (records)
        if role=="admin":
            if password=="Jr7+2m21" and username==records[0]:
                session["role"]=role
                session['login']=True
                error="Login succesful"
            else:
                error="Either username or password is incorrect"
        elif role=="user":   
            if records==[]:
                error="usernmae dosen't exits"
                return render_template("login.html",error=error)
                
            elif sha256_crypt.verify(password,records[1]) and username==records[0]:
                error="login sucssesful"
                session['login'] =True
                session["username"]=username
                
            else:
                error="Either username or password is incorrect"
    conn.close()        
    return render_template("login.html",error=error)         
    
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route('/display_feedback', methods=['GET', 'POST'])
def display_feedback():
    conn=sqlite3.connect("database/readersclub.db")
    cur=conn.cursor()
    cur.execute("Select * from feedback;")
    records=cur.fetchall()
    return render_template("display_feedback.html",records=records)


@app.route('/memberslist', methods=['GET', 'POST'])
def memberslist():
    conn=sqlite3.connect('database/readersclub.db')
    cur=conn.cursor()
    cur.execute("Select * from members_registration;")
    users=cur.fetchall()
    return render_template("memberslist.html",users=users)


if __name__ == "__main__":
    app.run(debug=True)

