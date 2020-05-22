from Client0 import Client

print(f"-----| Practice 2, Exercise 1 |------")

# -- Parameters of the server to talk to
ip = "192.168.1.38"
port = 8080

# -- Create a client object
create_client = Client(ip,port)

# -- Test the ping method
create_client.ping()

# -- Print the IP and PORTs
print(f"IP: {create_client.ip}, {create_client.port}")