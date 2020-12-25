import socket
import sys
import time
import errno
import math
from multiprocessing import Process

def process_start(s_sock):
    while True:
      s_sock.send(str.encode('Online Calculator\nChoose an operation [1-Log | 2-Sqrt | 3-Exp]\nPlease enter the operation number:'))
      while True:
        data = s_sock.recv(2048)
        data = data.decode('utf-8')
        print(data)
        if not data:
             break
        elif data == '1':
             s_sock.send(str.encode('Enter a number to calculate:'))
             num = s_sock.recv(2048)
             num = int(num)
             num = str(math.log(num))
             print(num)
             s_sock.send(str.encode('Answer:'+ num + '\nPress ENTER to continue'))
        elif data == '2':
             s_sock.send(str.encode('Enter a number to calculate:'))
             num = s_sock.recv(2048)
             num = int(num)
             num = str(math.sqrt(num))
             print(num)
             s_sock.send(str.encode('Answer:'+ num + '\nPress ENTER to continue'))
        elif data == '3':
             s_sock.send(str.encode('Enter a number to calculate:'))
             num = s_sock.recv(2048)
             num = int(num)
             num = str(math.exp(num))
             print(num)
             s_sock.send(str.encode('Answer:'+ num + '\nPress ENTER to continue.'))
        else:
             s_sock.send(str.encode('Error. Operation that you choose is not available.\nPress ENTER to continue.')) 
        break
       
         
 

    s_sock.close()
      


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("Listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('Got a socket error')

    except Exception as e:        
                print('An exception occurred!')
                print(e)
                sys.exit(1)
    finally:
     	   s.close()
