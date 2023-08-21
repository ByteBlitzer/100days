height = input('Enter your height in m: ')
weight = input('Enter your weight in kg: ')
output = float(weight) / float(height) ** 2
bmi = round(output)
print(bmi)
