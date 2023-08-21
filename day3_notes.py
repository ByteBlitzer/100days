water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("You can not ride the rollercoaster!")

number = int(input("Enter Number: "))
if number % 2 == 0:
    print("The number is even.")
elif number % 2 == 1:
    print("The number is odd.")
else:
    print("Try again.")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

print("which year do you want to check? ")
year = int(input("Enter year: "))

if year % 4 == 0: # if year is divisible by 4
    if year % 100 == 0: # if year is divisible by 100
        if year % 400 == 0: # if year is divisible by 400
            print("leap year") # if year is divisible by 4, 100 and 400
        else: 
            print("Not a leap year.") # if year is divisible by 4 and 100 but not 400
    else:
        print("leap year.") # if year is divisible by 4 but not 100
else:
    print("Not a leap year") # if year is not divisible by 4
    

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
        
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")
    
else:
    print("Sorry, you have to grow taller before you can ride.")


#  Don't change the code below 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# Don't change the code above 

#Write your code below this line 
size = size.upper()
add_pepperoni = add_pepperoni.upper()
extra_cheese = extra_cheese.upper()

small_pizza = 15
med_pizza = 20
large_pizza = 25
bill = 0

if size == "S":
    bill += small_pizza #if size is small, bill = 15
    if add_pepperoni == "Y": #if add_pepperoni is yes, bill = 15 + 2
        bill += 2 #bill = 17
    if extra_cheese == "Y": #if extra_cheese is yes, bill = 17 + 1
        bill += 1 #bill = 18
        
elif size == "M":
    bill += med_pizza #if size is medium, bill = 20
    if add_pepperoni == "Y": #if add_pepperoni is yes, bill = 20 + 3
        bill += 3 #bill = 23
    if extra_cheese == "Y": #if extra_cheese is yes, bill = 23 + 1
        bill += 1 #bill = 24
        
elif size == "L": #if size is large, bill = 25
    bill += large_pizza #if size is large, bill = 25
    if add_pepperoni == "Y": #if add_pepperoni is yes, bill = 25 + 3
        bill += 3 #bill = 28
    if extra_cheese == "Y": #if extra_cheese is yes, bill = 28 + 1
        bill += 1 #bill = 29
print(f"Your final bill is: ${bill}.") #print final bill

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = str(true + love)

print(love_score)
