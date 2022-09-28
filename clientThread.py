import socket

host='127.0.0.1'
port = 2022
print("Running Before connection")
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
message = "Hey Server!!! What will we do doing today's lab??"
while True:
    message=input("What you want to send?")
    s.send(message.encode("utf-8"))
    data=s.recv(1024)
    print("Message Received From server:",str(data.decode("utf-8")))
    reply = input("\n Do you want to continue(y/n) :")
    if(reply == "y"):
        continue
    else:
        print("Bye Server")
        break