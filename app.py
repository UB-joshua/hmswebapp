from flask import Flask,url_for
from flask import request,session
from flask.templating import render_template
import sqlite3
import pandas as pd

from flask_login import login_required,current_user
app=Flask(__name__)

@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/login')
def login():
    message="login here"
    return render_template('login.html',message=message)

@app.route('/register')
def register():
    return render_template('register.html')


@app.route("/registeruser", methods=['post'])
def my_register_page():
    entered_username=request.form.get("username")
    entered_password=request.form.get("password")
    entered_mobile=request.form.get("mobile")
    con=sqlite3.connect("hospital_database.sqlite3")
    cur=con.cursor()    # to execute queries like insert,update,delete,selet
    my_table_query="create table if not exists registered_users(name varchar(50),password number(10),mobile number(10))"

    cur.execute(my_table_query)
    cur.execute(f"select mobile from registered_users where mobile='{entered_mobile}'")
    
    result=cur.fetchone()
    if result!=None:
        return "Mobile Number already registered! try to login"
    else:
        cur.execute(f"insert into registered_users ('name','password','mobile') values ('{entered_username}','{entered_password}','{entered_mobile}')")
        
        con.commit()
        return "Succesfully Registered!"
        con.close()



@app.route("/validateuser", methods=['post'])
def my_login_page():
    entered_username=request.form.get("vusername")
    entered_password=request.form.get("vpassword")
    con=sqlite3.connect("hospital_database.sqlite3")
    cur=con.cursor()    # to execute queries like insert,update,delete,selet
    cur.execute(f"select * from registered_users where name='{entered_username}' and password='{entered_password}'")
    result=cur.fetchall()
    print(result)
    tempo=0
    for i in result:
        for j in i:
            if  j==9988776655:
                tempo=j
    print(tempo)
    # cur.execute(f"select mobile from registered_users where name='{entered_username}' and password='{entered_password}'")
    # res=cur.fetchall()
    print(result)
    # k=result[2]
    # k=str(k)
    # print(k)
    if result==None:
         message="Invalid Credentials"
         return render_template('login.html',message=message)
    elif entered_username=='admin' and entered_password=="admin@123" and tempo==9988776655:
         cur.execute(f"select * from registered_patients")
         myresult=cur.fetchall()
         #print(myresult)
         df=pd.DataFrame()
         for x in myresult:
            k=list(x)
            df2=pd.DataFrame({"name":[k[0]],"age":[k[1]],"disease":[k[2]],'phone':[k[3]],'date':[k[4]]})
            df=pd.concat([df,df2])
            df=df.rename(index={0:'.'})

         df.to_html('templates/allpatients_data.html')
         return render_template('allpatients_data.html')

    elif entered_username=='admin' and entered_password=="admin@123" and tempo!=9988776655:

         return render_template('patients_page.html')
    else:

         return render_template('patients_page.html')

@app.route("/user_booking",methods=['post'])
def user_booking_page():
    entered_patientname=request.form.get('patientname')
    entered_patientage=request.form.get("patientage")
    entered_disease=request.form.get("disease")
    entered_phone=request.form.get("phone")
    entered_date=request.form.get("date")
    conn=sqlite3.connect("hospital_database.sqlite3")
    cur=conn.cursor()
    #cur.execute("drop table registered_patients")
    my_query="create table if not exists registered_patients(patient_name varchar(50),patient_age number(10),patient_disease varchar(10),phone number(10),date varchar(20) )"

    cur.execute(my_query)
    cur.execute(f"select date from registered_patients where date='{entered_date}'")
    result=cur.fetchone()
    if result!=None:
        messages="appointment already booked for the given time"
        return render_template('bookings.html',messages=messages)
    
    else:
        cur.execute(f"insert into registered_patients('patient_name','patient_age','patient_disease','phone','date') values ('{entered_patientname}','{entered_patientage}','{entered_disease}','{entered_phone}','{entered_date}')")
        
        conn.commit()
        return "Succesfully Booked!"
        conn.close()



@app.route('/booking_details')
def booking_details():
    return render_template('booking_details.html')


@app.route('/bookings')
def bookings():
    messages="Enter Booking details"
    return render_template('bookings.html',messages=messages)

@app.route('/services')
def services():
    return render_template('services.html')

# def logout():
#     render_template('index.html')


@app.route("/booked_details",methods=['post'])
def details():
    patientname=request.form.get('patient_name')

    conn=sqlite3.connect("hospital_database.sqlite3")
    cur=conn.cursor()
    
    compar=(f"select patient_name from 'registered_patients'")
    cur.execute(compar)
    ptnames=cur.fetchall()

    n=[]
    for i in ptnames:
        n.append("".join(i))
    if patientname in n:
        cur.execute(f"select * from registered_patients where patient_name='{patientname}'")
        d=cur.fetchall()
        

        [newl]=d
        r= "  name : {}\n\n  age : {}\n\n  disease : {}\n\n  phone : {}\n\n  appointment_date: {}".format(newl[0],newl[1],newl[2],newl[3],newl[4])
        return r
            


    else:
        
        return "Patient Data not found" 
 
  
    
    

    # if patientname==compar:
    #     query=(f"SELECT * FROM registered_patients where patient_name=='{patientname}'")
    #     res=cur.execute(query)
    #     return res

    # else:
    #     message="patient data not found"
    #     return render_template('booking_details.html',message=message)

    conn.close()
    










if __name__  ==  '__main__':
    app.run(debug=True)