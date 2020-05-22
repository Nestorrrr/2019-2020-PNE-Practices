from Client0 import Client

print(f"-----| Practice 3, Exercise 7 |------")

IP = '127.0.0.1'
PORT = 8080

c = Client(IP,PORT)
print(c)

# -- Test 1: Ping
print("* Testing PING...")
print(c.talk('PING'))

# -- Test 2: Get
print("* Testing GET...")
for i in range(5):
    cmd = f"GET {i}"
    print(f'{cmd}: {c.talk(cmd)}', end='\n')
