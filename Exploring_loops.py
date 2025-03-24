# Write a For loop
for i in [1, 2, 3 , 4]:
    print (i)

# Run a for loop with range
for i in range (4):
    print ("I cannot connect to the destination")
# This message will be returned 4 times

# Write a While loop
time = 0
while time < 10:
    print (time)
    time = time + 2
# Time will increase by a value of 2 until it gets to a value of 10

max_devices = 5
i = 1
while i < max_devices:
    print ("user can still connect to additional devices")
    i = i + 1
print ("User has reached the maximum number of connected devices")

# Use break to break out of a loop
computer_assets = ["laptop 1", "desktop 20", "smartphone 03"]
for asset in computer_assets:
    if asset == "desktop 20":
        break
    print (asset)
# The loop will end after laptop 1

# Use continue to skip an iteration and continue with the next one
computer_assets = ["laptop 1", "desktop 20", "smartphone 03"]
for asset in computer_assets:
    if asset == "desktop 20":
        continue
    print (asset)
# The loop will skip desktop 20