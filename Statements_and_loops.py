# Write a conditional statement
failed_attempts = 3
if failed_attempts > 5:
    print ("Account locked")
# Python will return the account locked message if login attempts is greater than 5

operating_system = "OS 2"
if operating_system == "OS 2":
    print ("Updates needed")

# Add an else statement
operating_system = "OS 2"
if operating_system == "OS 2":
    print ("Updates needed")
else :
    print ("No updates needed")

# Use elif
status = 300
if status == 200:
    print ("OK")
elif status == 400:
    print ("Bad request")
elif status == 500:
    print ("Internal server error")
else:
    print ("Check other status")

# Use and
status = 205
if status >= 200 and status <= 226:
    print ("Successful response")

# Use or
status = 100
if status == 100 or status == 102:
    print ("Informational response")

# Use not
status = 205
if not (status >= 200 and status <= 226):
    print ("Check status")
# Check status message will be returned if the status is less than 200 or greater than 226

# Use in
approved_list = ["Stephanie", "Jojo", "Joice", "Melody"]
username = "Jojo"
if username in approved_list:
    print ("This user has approved access to this device")
else:
    print ("This user does not have approved access to this device")