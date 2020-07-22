import smtplib
email="shyamendra99@gmail.com"
password="g_mail.com@123"
send_mail="bharat8249@gmail.com"
text="your server is working fine "


server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(shyamendra99@gmail.com,g_mail.com@123)
server.sendmail(email, bharat8249@gmail.com, text)
server.quit()
