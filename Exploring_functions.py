# Define a function
def greet_employee ():
    print ("Welcome! You're logged in.")

# Call a function
greet_employee ()

# Define a function and incorporate a variable
def display_investigation_message ():
    print ("Investigate activity")

applicaion_status = "potential concern"
email_status = "okay"

if applicaion_status == "potential concern":
    print ("application_log")
    display_investigation_message ()

if email_status == "potential concern":
    print ("email log:")

# Use parameters in functions
# Greet employees by name
def greet_employee (name):
    print ("Welcome! You're logged in", name)

greet_employee ("Charley Patel")

def greet_employee (first_name, last_name):
    print ("Welcome! You're logged in", first_name, last_name)

greet_employee ("Kiara", "Carter")

# Return information from a function
def calculate_fails (total_attempts, failed_attempts):
    fail_percentage = failed_attempts/ total_attempts
    return fail_percentage

percentage = calculate_fails (4,2)

if (percentage >= .5):
    print ("Account locked.")

# Use max
a = 3
b = 9
c = 6
print (max(a, b, c))

# Use min
a = 1
b = 10
c = 4
print (min(a, b, c))

# Use sorted
usernames = ["Sophie", "Angela", "Nathan", "Jonathan"]
print (sorted(usernames))