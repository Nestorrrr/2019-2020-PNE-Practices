from Client0 import Client

print(f"-----| Practice 3, Exercise 7 |------")

IP = '127.0.0.1'
PORT = 8080

# -- Cofigure the client
c = Client(IP, PORT)
print(c.talk('Hello'))