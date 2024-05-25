a=1
b=2
print a+b
from _thread import *
import threading

print_lock = threading.Lock()
##############################
### support json query

def threaded (conn):
   while True:
    data = conn.recv(1024)
    print data
    print len(data)
    print "################"
    if (data.startswith("GET")):
      if "9999" in data: break
      if not ("HTTP/" in data):
         data="GET /startp2.html HTTP/1.1"
         print "send startp2.html again"
      
      data_sub=data.split("HTTP/")
      data_sub=data_sub[0].split(" ")
      flag1="not_file_loaded"
      if (data_sub[1].endswith(".txt")):
         header="HTTP/1.1 200 OK\n"
         header= header + "Content-Type: text/html\n\n"
         header=header.encode('utf-8')
         file_data3=GETFILENAME(data_sub[1].replace("/",""))
         file_data1 = header + file_data3
         flag1="file_loaded"
      if (data_sub[1].endswith(".json")):
         header="HTTP/1.1 200 OK\n"
         header= header + "Content-Type: text/html\n\n"
         header=header.encode('utf-8')
         file_data3=GETFILENAME(data_sub[1].replace("/",""))
         file_data1 = header + file_data3
         flag1="file_loaded"
      if (data_sub[1].endswith(".jpg")):
         header="HTTP/1.1 200 OK\n"
         header= header + "Content-Type: image/jpg\n\n"
         header=header.encode('utf-8')
         file_data3=GETFILENAME(data_sub[1].replace("/",""))
         file_data1 = header + file_data3
         flag1="file_loaded"
      if (data_sub[1].endswith(".js")):
         header="HTTP/1.1 200 OK\n"
         header= header + "Content-Type: text/javascript\n\n"
         header=header.encode('utf-8')
         file_data3=GETFILENAME(data_sub[1].replace("/",""))
         file_data1 = header + file_data3
         flag1="file_loaded"
      if (data_sub[1].endswith(".css")):
         header="HTTP/1.1 200 OK\n"
         header= header + "Content-Type: text/css\n\n"
         header=header.encode('utf-8')
         file_data3=GETFILENAME(data_sub[1].replace("/",""))
         file_data1 = header + file_data3
         flag1="file_loaded"
      if (data_sub[1].endswith(".html")):
         header="HTTP/1.1 200 OK\n"
         header= header + "Content-Type: text/html\n\n"
         header=header.encode('utf-8')
         file_data3=GETFILENAME(data_sub[1].replace("/",""))
         file_data1 = header + file_data3
         flag1="file_loaded"
      if (data_sub[1]=='/'):
         header="HTTP/1.1 200 OK\n"
         header= header + "Content-Type: text/html\n\n"
         header=header.encode('utf-8')
         file_data3=GETFILENAME("startp2.html")
         file_data1 = header + file_data3
         flag1="file_loaded"
      if (flag1=="not_file_loaded"):
         header="HTTP/1.1 200 OK\n"
         header= header + "Content-Type: text/html\n\n"
         header=header.encode('utf-8')
         file_data3="Error, content type not found 456\n"
         file_data1 = header + file_data3
         flag1="file_loaded"
      conn.send(file_data1)
      conn.close()
    if (data.startswith("POST")):
       WBOUNDARY=0
       if ("WebKitFormBoundary" in data):
          WBOUNDARY=1
    if not ((data.startswith("POST")) or (data.startswith("GET"))):
      if (WBOUNDARY==0):
        header="HTTP/1.1 200 OK\n"
        header= header + "Content-Type: text/html\n\n"
        header=header.encode('utf-8')
        file_data3=GETFILENAME("test2.html")
        file_data1 = header + file_data3
        flag1="file_loaded"
        conn.send(file_data1)
        conn.close()
        WBOUNDARY=5
        print "closed connection WBOUNDARY 0"
      if (WBOUNDARY==3):
        WBOUNDARY=5
        conn.close()
        print "closed connection WBOUNDARY 3"
      if (WBOUNDARY==2):
        if ("WebKitFormBoundary" in data):
           WBOUNDARY=3
           header="HTTP/1.1 200 OK\n"
           header= header + "Content-Type: text/html\n\n"
           header=header.encode('utf-8')
           file_data3=GETFILENAME("test2.html")
           file_data1 = header + file_data3
           flag1="file_loaded"
           conn.send(file_data1)
           conn.close()
      if (WBOUNDARY==1):
        if ("WebKitFormBoundary" in data):
           WBOUNDARY=2

   
###############################
def GETFILENAME(filename):
   try :
      f3=open(filename, "rb")
      getf3=f3.read()
      f3.close()
      return getf3
   except :
      getf3="Error, content not found 404\n"
      return getf3

##############################



##############################
import socket
HOST = "0.0.0.0"
PORT = 8080
data="test"
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
while 1:
      conn, addr = s.accept()
      print "connected by ", addr
      start_new_thread (threaded, (conn,))
s.close()
exit()
