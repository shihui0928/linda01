from HTMLTestRunner import HTMLTestRunner
import unittest,time,os
from public import global_params as gp
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


if __name__ =="__main__":
    gp._init()
    gp._init2()
    gp._init3()

    now=time.strftime("%y-%m-%d %H_%M_%S" )
    filename="report\\"+now+" result.html"
    # filename="report\\"+"result.html"



    fp=open(filename,"wb")
    runner=HTMLTestRunner(stream=fp,title="接口报告测试")
    discover=unittest.defaultTestLoader.discover("./testcase",pattern="*test.py")
    runner.run(discover)
    fp.close()

    #---1、跟发件相关的参数
    smtpserver="smtp.163.com"
    # port=0 #不需要端口
    sender="fei01a02@163.com"
    psw="abc123"  #//邮箱的第三方客户端授权密码
    receiver= '68865309@qq.com'

    path=r"C:\Users\hui.shi\PycharmProjects\untitled1\report"
    list0=os.listdir(path) #返回测试报告所在目录下的所有文件列表
    list=sorted(list0) #获得按升序排序后的测试报告列表
    file_new=os.path.join(path,list[-1])#获取最后一个即最新的测试报告地址
    print(type(list0))
    print(type(list))




    #----2.编辑邮件的内容--
    file_path=file_new
    with open(file_path,"rb") as fp:
        mail_body=fp.read()
    msg=MIMEMultipart()
    subject="这个是主题163"
    body="<p>这个是发送的163邮件</p>"
    # msg=MIMEText(body,"html","utf-8")
    msg["From"]="fei01a02@163.com"
    msg["To"]=  '68865309@qq.com'
    msg["Subject"]=subject
    body=MIMEText(body,"html","utf-8")
    msg.attach(body)

    #--附件
    att=MIMEText(mail_body,"base64","utf-8")
    att["Content-Type"]="application/octet-stream"
    att["Content-Disposition"]='attachment;filename="test_report.html"'
    msg.attach(att)
    #--3.发送邮件
    try:
        smtp=smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(sender,psw)
    except:
        smtp=smtplib.SMTP_SSL(smtpserver)
        smtp.login(sender,psw)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()




# def all_case():
#
#     testcase=unittest.TestSuite()
#     discover=unittest.defaultTestLoader.discover(case_dir,pattern="*test.py")
#
#     # for test_suite in discover:
#     #     for test_case in test_suite:
#     #         testcase.addTests(test_case)
#     #
#     # print(testcase)
#     # return testcase
#     testcase.addTests(discover)
#     return testcase
#
# if __name__ =="__main__":
#     gp._init()
#     gp._init2()
#     gp._init3()
#     now=time.strftime("%y-%m-%d %H_%M_%S" )
#     filename="report\\"+now+" result.html"
#
#     fp=open(filename,"wb")
#     runner=HTMLTestRunner(stream=fp,title="接口报告测试")
#     case_dir="C:\\Users\\hui.shi\\PycharmProjects\\untitled1\\testcase"
#     runner=unittest.TextTestRunner()
#     runner.run(all_case())
#     fp.close()

