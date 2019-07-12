import smtplib
import config
content = 'hii,how are you'
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(config.EMAIL_ADDRESS,config.PASSWORD)
n = input('enter the recipents gmail address')
header = 'To:' + n + '\n' + 'From:' + config.EMAIL_ADDRESS + '\n' + 'Subject:testing\n'
content = header + content
mail.sendmail(n,config.EMAIL_ADDRESS,content)
mail.close()
