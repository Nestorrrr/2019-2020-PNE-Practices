from Client0 import Client

print(f"-----| Practice 3, Exercise 7 |------")

IP = '127.0.0.1'
PORT = 8080

# -- Cofigure the client
c = Client(IP, PORT)
print(c)

# -- Test 1: Ping
print("* Testing PING...")
print(c.talk("PING"))

# -- Test 2: Get
print("* Testing GET...")
for i in range(5):
    cmd = f"GET {i}"
    print(f"{cmd}: {c.talk(cmd)}", end="")

# -- Get the sequence 0 for testing
seq = c.talk("GET 0")
print()

# -- Test 3: INFO
print("* Testing INFO...")
cmd = f"INFO {seq}"
print(c.talk(cmd))

# -- Test 4: COMP
print("* Testing COMP...")
cmd = f"COMP {seq}"
print(cmd, end="")
print(c.talk(cmd))

# -- Test 5: REV
print("* Testing REV...")
cmd = f"REV {seq}"
print(cmd, end="")
print(c.talk(cmd))

# -- Test 6: GENE
print("* Testing GENE...")
for gene in ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]:
    cmd = f"GENE {gene}"
    print(cmd)
    print(c.talk(cmd))