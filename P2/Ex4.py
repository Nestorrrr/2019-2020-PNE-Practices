from Client0 import Client

print(f"-----| Practice 2, Exercise 4 |------")

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)

c.debug_talk("Message 1---")
c.debug_talk("Message 2: Testing !!!")