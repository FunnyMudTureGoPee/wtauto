import datetime
 
from threading import Timer
 
def time_printer():
 
    now = datetime.datetime.now()
 
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
 
    print('do func time :', ts)
 
    loop_monitor()
 
def loop_monitor():
 
    t = Timer(5, time_printer)
 
    t.start()
 
if __name__ == "__main__":
 
    loop_monitor()