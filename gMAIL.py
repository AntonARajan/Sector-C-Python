#!/usr/bin/python3
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("josidart@gmail.com", x=input("Enter your password:"))
message = "hi Anton, You are a part of ME, but.. you've just been hacked!!!"
server.sendmail("josidart@gmail.com", "antonrajan18@gmail.com", message) 
server.quit()




