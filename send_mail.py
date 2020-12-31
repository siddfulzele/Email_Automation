import pandas as pd
import smtplib

link ="https://forms.gle/aikahxBhaTV6QHPFA"
image = "dostipine_projectelevation.jpg"
filepath = "C:/Users/Sidd/Desktop/project/email/sendinblue/1st_300.csv"
sender = 'siddfulzele@gmail.com'
emails = pd.read_csv(filepath,header=None)
emails = list(emails[0])

message = """From: Siddhant Fulzele <from@fromdomain.com>
To: Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: Dosti Pine Project

<center>
<a href="""+link+""">
<img src="https://raw.githubusercontent.com/siddfulzele/Temp/master/"""+image+"""" alt="This IS Image1">
<br>
<img style="width: 100%;
  max-width: 800px;
  height: auto;" src="https://raw.githubusercontent.com/siddfulzele/Temp/master/dosti_pine.jpg" alt="This IS Image">
</a>
<br>
<a href="""+link+""" ><button style="background-color: #4CAF50;
  border: none;
  color: white;
  padding: 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;border-radius: 8px;">Click Here for Open Link</button></a>
</center>
regards"""

count = 0
for email in emails:
   count = count +1
   print(count)
   try:
      smtpObj = smtplib.SMTP('smtp.gmail.com:587')
      smtpObj.ehlo()
      smtpObj.starttls()
      smtpObj.login(sender,"***password***")
      smtpObj.sendmail(sender, email, message)
      smtpObj.quit()

      print("Successfully sent email")
   except SMTPException:
      print("Error: unable to send email")

