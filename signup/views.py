import mysql.connector
from django.shortcuts import render, redirect, get_object_or_404

from hashlib import md5





def signAction(request):

    if request.method=='POST':
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            sex = request.POST.get('sex')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password_hash = md5( password.encode("utf-8") ).hexdigest()




            mydb  = mysql.connector.connect(
                user='root',
                password='aspire4730z',
                host='127.0.0.1',
                database='presensi'
            )
            mycursor = mydb.cursor()
            sql = (
                "INSERT INTO users(firstname, lastname, sex, email, password)"
                "VALUES (%s, %s, %s, %s, %s)"
            )
            val = (firstname, lastname, sex, email, password_hash)
            mycursor.execute(sql, val)
            mydb.commit()

            return redirect("/")
    return render(request,"signup_page.html")
