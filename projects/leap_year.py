#Write a program that works out whether if a given year is a leap year. 
# A normal year has 365 days, leap years have 366, with an extra day in February. 
# The reason why we have leap years is really fascinating

#on every year that is evenly divisible by 4 
#**except** every year that is evenly divisible by 100 
#**unless** the year is also evenly divisible by 400

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("Not leap year.")
    else:
        print("leap year.")
else:
    print("Not leap year")





    


    



    



