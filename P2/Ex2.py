from Client0 import Client

print(f"-----| Practice 2, Exercise 2 |------")

# -- Parameters of the server to talk to
ip = "127.0.0.1"
port = 8080

# -- Create a client object
create_client = Client(ip,port)

print(create_client)
