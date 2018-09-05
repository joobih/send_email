import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.header import Header
import smtplib


def SendEmail(toAdd, subject, htmlText):
    """
    :param toAdd:   目的邮箱
    :param subject: 邮件主题
    :param htmlText:    邮件正文
    """
    import smtplib
    server = "smtp.sina.com"
    fromaddr = "joobih@sina.com"  # 须修改
    msg = MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = Header(fromaddr)

    content1 = MIMEText(htmlText, 'plain', 'utf-8')
    msg.attach(content1)

    s = smtplib.SMTP(server)
    s.set_debuglevel(1)
    s.login("joobih@sina.com", "password") # 须修改新浪密码
    s.sendmail(fromaddr, [toAdd], msg.as_string())
    s.close()

if __name__ == '__main__':
    strTo = "1006536507@qq.com"
    subject = u"测试"
    html = "发送的测试邮件"
    SendEmail(strTo, subject=subject, htmlText=html)