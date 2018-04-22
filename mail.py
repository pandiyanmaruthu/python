import smtplib
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("maruthu@integrityindia.com","ubuntu14.04")
msg="""
Test Mail from python"""
subject="Reg:Python Mail"
message="Subject:{}\n\n{}".format(subject,msg)
server.sendmail("maruthu@integrityindia.com","pandiyanmaruthu6@gmail.com",message)
server.quit()

