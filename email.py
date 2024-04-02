import smtplib
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP 환경 변수
# SMTP_SERVER = os.environ.get('SMTP_SERVER')
# SMTP_PORT = os.environ.get('SMTP_PORT')
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
# SMTP_USER = os.environ.get('SMTP_USER')
# SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')
SMTP_USER = 'gntodtndls156@gmail.com'
SMTP_PASSWORD = 'geuvzzurymgtlisp'

# Email Form
to_addr = input('이메일 입력하세요:')

## content
msg = MIMEMultipart()
msg['From'] = SMTP_USER
msg['To'] = to_addr
msg['Subject'] = '제목'

msg_body = f"""
<body style="font-family: Arial, sans-serif; background-color: #f4f4f4;">
    <div style="max-width: 600px; margin: 0 auto; background-color: white; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
      <h1 style="color: #333;">책 추천</h1>
      <div style="border: 1px solid #ddd; padding: 10px; margin-bottom: 20px; display: flex; align-items: center;">
        <img style="width: 100px; height: auto; margin-right: 20px;" src="https://example.com/book-cover.jpg" alt="책 표지">
        <div>
          <h2 style="margin-top: 0;">책 제목</h2>
          <p style="line-height: 1.5; color: #666;">저자 정보</p>
          <p style="line-height: 1.5; color: #666;">책 소개</p>
          <p style="line-height: 1.5; color: #666;"><a href="#" style="color: #007bff; text-decoration: none;">책 링크(short url)</a></p>
        </div>
      </div>
    </div>
  </body>
"""
html = MIMEText(msg_body, 'html', _charset='UTF-8')
msg.attach(html)

## send
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login(SMTP_USER, SMTP_PASSWORD)
smtp.sendmail(SMTP_USER, to_addr, msg.as_string())
smtp.close()