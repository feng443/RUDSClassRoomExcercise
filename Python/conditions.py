# 1.
x = 5
y = 10
if (2 * x > 10):
    print("Question 1 works!")
else:
    print("oooo needs some work")  # This!

# 2.
x = 5
y = 10
if (len("Dog") < x):
    print("Question 2 works!")  # This!
else:
    print("Still missing out")

# 3.
x = 2
y = 5
if ((x**3 >=y) and (y**2 < 26)): # T
    print("GOT QUESTION 3!") # This!
else:
    print("Oh good you can count")

# 4.
name = "Dan"
group_one = ["Greg", "Tony", "Susan"]
group_two = ["Gerald", "Paul", "Ryder"]
group_three = ["Carla", "Dan", "Jefferson"]

if (name in group_one):  # False
    print(name + " is in the first group")
elif (name in group_two): # False
    print(name + " is in group two")
elif (name in group_three): # True
    print(name + " is in group three") # This!
else:
    print(name + " does not have a group")


# 5.
height = 66
age = 16
adult_permission = True

if ((height > 70) and (age >=18)):  # Fale
    print("Can ride all the roller coasters")
elif ((height > 65) and (age >=18)): # False
    print("Can ride moderate roller coasters")
elif ((height > 60) and (age >= 18)): # False
    print("Can ride light roller coasters")
elif (((height > 50) and (age >= 18)) or ((adult_permission) and (height > 50))):   # True
    print("Can ride bumper cars")   # This!
else:
    print("Sitck to lazy river")