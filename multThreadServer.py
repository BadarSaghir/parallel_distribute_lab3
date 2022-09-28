# from asyncio.trsock import _RetAddress
import socket
import threading

print_lock = threading.Lock();
def createThread(c, addr):
    print(f"New Connection : {addr}")
    print("Thread Name : ",threading.current_thread().getName())
    while True:
        data = c.recv(1024)
        print("Received From client ",str(data.decode("utf-8")))
        if not data or str(data.decode("utf-8")).lower()=="bye":
            print("Bye!")
            # print_lock.release()
            c.close()
            break
        data= "I am server, Ok, great I have you message : "+str(data.decode("utf-8"))
        c.send(data.encode("utf-8"))
    c.close()

def main():
    host = "localhost"
    port= 2022
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host,port))
    print("Socket is listening for incoming connection")
    s.listen(10)
    while True:
        c, addr= s.accept()
        # print_lock.acquire()
      
        print("Connected To:",addr[0],addr[1])
        print(f"Threading, before creating thread :",threading.current_thread().getName())
        thread= threading.Thread(target=createThread,args=(c,addr))
        thread.start()
    s.close()

main()

