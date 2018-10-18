import socket
import sys


# Usage: command line 
# > python ic-ping.py google.com:80 yahoo.com:80 mysql.com:3306

# Usage: hard coded 
# Fill out the hc_list array:
# hc_list = ["www.google.com:80", "mysql.com:3306", "www.lfdskgjdsa.com:80"]
# > python ic-ping.py

# if both are done, command line will win 


hc_list = []


if len(sys.argv) > 1:
    todo = []
    c = 0
    for item in sys.argv:
        if c!= 0:
            todo.append(item)
        c+=1         
else:
    todo = hc_list




def isOpen(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(10)
        s.connect((ip, int(port)))
        s.settimeout(None)
        s.shutdown(2)
        return True
    except:
        return False


class ColorPrint:

    @staticmethod
    def print_fail(message, end = '\n'):
        sys.stderr.write('\x1b[1;31m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_pass(message, end = '\n'):
        sys.stdout.write('\x1b[1;32m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_warn(message, end = '\n'):
        sys.stderr.write('\x1b[1;33m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_info(message, end = '\n'):
        sys.stdout.write('\x1b[1;34m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_bold(message, end = '\n'):
        sys.stdout.write('\x1b[1;37m' + message.strip() + '\x1b[0m' + end)




g = 0
b = 0
pr = ColorPrint

for i in todo:
    ip, port = i.split(':')
    pr.print_info('testing '+ip+' on '+port) 
    if isOpen(ip, port):
        pr.print_pass("-->reached "+ip+" on "+port) 
        g+=1
    else:
        pr.print_fail("-->not able to reach "+ip+" on "+port)
        b+=1

pr.print_info(str(g)+' tests passed, '+str(b)+' tests failed.')



