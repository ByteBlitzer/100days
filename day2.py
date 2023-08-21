# num_char = len(input("What's you name? "))
# new_num_char = str(num_char)
# print("Your name contains " + new_num_char + "characters")

# a = float(123)
# print(type(a))

# print(70 + float("100.5"))

# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]
# result = int(first_digit) + int(second_digit) # Convert to int to add the digits together, if string it would just join
# print(result)

3 + 5
7 - 3
3 * 2
6 / 3       # Divide always float / decimal
2 ** 2      # 2 x 2

PEMDAS-LR
Parentheses ()    |    ()
Exponents **      |    **
Multiplication *  |    * /
Division /        |    + -
Addition +
Subtraction -

3 * 3 + 3 / 3 - 3
# Output: 7.0
3 * (3 + 3) / 3 - 3
# Output: 3.0

BMI = weight / height ** 2  # 70 / 1.8 ** 2 = 21.6
height = input('Enter your height in m: ')  
weight = input('Enter your weight in kg: ') 
output = float(weight) / float(height) ** 2
bmi = round(output) # round() rounds to nearest whole number
print(bmi)

print(int(8/3)) # Output: 2
print(round(8/3, 2)) # Output: 2.67
print(8//3) # Output: 2

result = 4 / 2 # 2.0
result /= 2  # 1.0 
# divides result by 2 and assigns it to result / result = result / 2

score = 0 # sets score to 0

# User scores a point
score += 1 # adds 1 to score
score -+ 1 # subtracts 1 from score
score *= 2 # multiplies score by 2
score /= 2 # divides score by 2


score = 0
height = 1.8
is_winning = True
# f-String
f"your score is" # this is a f-string
print(f"your score is {score}, your height is {height}, you are winning is {is_winning")

print("Your score is " + str(score)) # Output: Your score is 0

# Create a program using maths and f-string that tells us how many days, weeks,
# months we have left if we live to 90.

# It will take your current age as input and output a message with our time left
# Format: You have x days, y weeks and z months

# Example:
# You have 12410 days, 1768 weeks, and 408 months left.

days = 365
weeks = 52
months = 12

days_in_life = days * 90
weeks_in_life = weeks * 90
months_in_life = months * 90

user_age_days = days * int(age)
user_age_weeks = weeks * int(age)
user_age_months = months * int(age)

days_left = days_in_life - user_age_days
weeks_left = weeks_in_life - user_age_weeks
months_left = months_in_life - user_age_months
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")

#Shorter way to do it
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = (f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months.")
print(message)

12 percent tip would be 12 / 100
150 * 12 = 18.0
150 + 18 = 168
# Simple way 150 * 1.12

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.

#Write your code below this line 

print("Welcome to the tip calculator.")
bill = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? 10 or 12? ")
people_to_split = input("How many people to split the bill? ")

people_to_split = int(bill) / 5
tip = int(people_to_split) * 1.12
final_amount = "{:.2f}".format(tip)
print(f"Each person should pay {final_amount}")



