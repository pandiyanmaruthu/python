import smtplib
sender='pandiyanmaruthu6@gmail.com'
receivers=["maruthu@integrityindia.com","pandiyanmaruthu6@outlook.com"]
message="""
From:maruthu<maruthu@integrityindia.com>
To:pandiyan<maruthu@integrityindia.com>
Subject:"Test Messages From Maruthu
"""
try:
    mail=smtplib.SMTP('localhost')
    mail.sendmail(sender,receivers,message)
    print "Mail Send Successfull"
except:
    print ("Can't send email....")
