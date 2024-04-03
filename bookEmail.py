import smtplib
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# type
from bookRecommender import RecommendBook

# smtp config
def getServer():
    return os.environ.get('SMTP_SERVER')

def getPort():
    return os.environ.get('SMTP_PORT')

def getUserEmail():
    return os.environ.get('SMTP_USER')

def getUserPassword():
    return os.environ.get('SMTP_PASSWORD')

# SMTP 환경 변수
# SMTP_SERVER = 'smtp.gmail.com'
# SMTP_PORT = 465
# SMTP_USER = 'gntodtndls156@gmail.com'
# SMTP_PASSWORD = 'geuvzzurymgtlisp'

def sendEmail(to_addr, book : RecommendBook):
    # Email Form
    title = book.get_name()
    body = book.get_bInfo().replace('\n', '<br>')
    image = book.get_image()
    writer = book.get_writer()
    url = book.get_url()
    
    ## content
    msg = MIMEMultipart()
    msg['From'] = getUserEmail()
    msg['To'] = to_addr
    msg['Subject'] = title

    msg_body = f"""
    <body style="font-family: Arial, sans-serif; background-color: #f4f4f4;">
        <div style="max-width: 1200px; margin: 0 auto; background-color: white; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
          <h1 style="color: #333;">책 추천</h1>
          <div style="border: 1px solid #ddd; padding: 10px; margin-bottom: 20px; display: flex; align-items: center;">
            <img style="width: 380px; height: 557px; margin-right: 20px;" src="{image}" alt="책 표지">
            <div>
              <h2 style="margin-top: 0;">{title}</h2>
              <p style="line-height: 1.5; color: #666;">{writer}</p>
              <p style="line-height: 1.5; color: #666;">{body}</p>
              <p style="line-height: 1.5; color: #666;"><a href="{url}" style="color: #007bff; text-decoration: none;">책 링크</a></p>
            </div>
          </div>
        </div>
      </body>
    """
    html = MIMEText(msg_body, 'html', _charset='UTF-8')
    msg.attach(html)

    ## send
    smtp = smtplib.SMTP_SSL(getServer(), getPort())
    smtp.login(getUserEmail(), getUserPassword())
    smtp.sendmail(getUserEmail(), to_addr, msg.as_string())
    smtp.close()