import smtplib
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("pandiyanmaruthu6@gmail.com","REDHATRHCE7")
sender="pandiyanmaruthu6@gmail.com"
to=["maruthu@integrityindia.com","pandiyanmaruthu@outlook.com"]
msg=""" Test email from python
"""
subject="Python Email"
message="Subject:{}\n\n{}".format(subject,msg)
try:
    server.sendmail(sender,to,message)
    print("Mail Sent Successfully")
except:
    "Error, TryAgain"
server.quit()