from socket import *
from threading import *


open_ports = []

def scan(ip,port):

    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((ip, port))
        print ('Scanning ', ip , 'on port',  port)
        print("Port",port, "is open")
        s.close()
        summary(port)

    except:
        print ('Scanning ', ip , 'on port',  port)
        print("Port",port,"is closed")

    finally:
        s.close()

def loop():

    for i in range(1,100):
        ip = '127.0.0.1'
        port = int(i)
        t = Thread(target=scan, args=(ip,int(port)))
        t.start()

    return

def summary(port):

    global open_ports
    open_ports.append(port)
    return      

def main():    
    loop()
    finish()

def finish():

    print('The following ports are open:',open_ports) 


main()
