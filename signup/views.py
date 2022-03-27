
from django.shortcuts import render


import mysql.connector as sql
fn=''
ln=''
s=''
em=''
pwd=''



# Create your views here.
def signAction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="aspire4730z",database="presensi")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="firstname":
                fn=value
            if key=="lastname":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value

        c="INSERT INTO `presensi`.`users` (`firstname`, `lastname`, `sex`, `email`, `password`) VALUES (fn, ln, s, em, MD5(pwd))"
        cursor.execute(c)
        m.commit()   
    return render (request,'signup_page.html')               
