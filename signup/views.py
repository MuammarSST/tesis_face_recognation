import mysql.connector
from django.shortcuts import render, redirect, get_object_or_404

from hashlib import md5

from signup.forms import BiodataUser



def signAction(request):
    form=BiodataUser(request.POST)
    if request.method=='POST':
        if form.is_valid():

            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            sex = form.cleaned_data['sex']
            email = form.cleaned_data['email']
            password = form.cleaned_data['email']
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
        pass
    return render(request,"signup_page.html")
