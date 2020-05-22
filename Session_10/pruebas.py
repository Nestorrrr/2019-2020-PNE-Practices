from Client0 import Client

print(f"-----| Practice 2, Exercise 3 |------")

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)

print(c)
# -- Send a message to the server
print("Sending a message to the server...")
response = c.talk(input('Type here: '))
print(f"Response: {response}")
