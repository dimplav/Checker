import connection
from apscheduler.schedulers.blocking import BlockingScheduler
import threading
string1 = ""
string2 = ""
changed = False
def fja(string):
    global string1
    global string2
    global changed
    string2 = string
    if string1 == string2:
        print("Stringovi su isti")
        string1 = string2
        string2 = string
        changed = False
    else:
        print("Stringovi nisu isti")
        string1 = string2
        string2 = string
        changed = True


def some_job():
    str = connection.listajLinkove()
    fja(str)

scheduler = BlockingScheduler()

def check():
    global scheduler
    scheduler.add_job(some_job, 'interval', minutes=0.1)

    scheduler.start()

def escape():
    global scheduler
    scheduler.remove_all_jobs()

t1 = threading.Thread(target=check)
t2 = threading.Thread(target=escape)
def nit():
    global string1
    string1 = connection.listajLinkove()
    t1.start()

def nit1():
    t2.start()


def links():
    print("link")
    connection.tag = 'a'
def images():
    print("images")
    connection.tag = 'img'

