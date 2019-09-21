username = input ("Username: ")
password = input ("Password: ")
while True:
    repass = input ("Retype password: ")
    if repass != password:
        print ("Wrong password")
    else:
        email = input ("E-mail: ")
        if "@" in email and "." in email:
            print ("success")
