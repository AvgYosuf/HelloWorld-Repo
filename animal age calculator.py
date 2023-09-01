"""
Joe Burns
08/31/23
Human -> animal age convertor
"""

hum_age = -1.0
ani_age1 = -1.0
ani_age2 = -1.0
ani_age3 = -1.0
years = -1.0
yr_rem = -1.0
months = -1.0
month_rem = -1.0
days = -1.0

print('Hello human! Enter your age if you are curious to learn how old you are in animal years')

hum_age = float(input()) #user input age in years

ani_age1 = hum_age * 7 #store age
years = ani_age1 // 1 #calculate and store new age 
yr_rem = ani_age1 % 1 #calculate and store remainder for next expression
months = yr_rem * 12 // 1 #calculate and store months 
month_rem = yr_rem * 12 % 1 #calculate and store remainder for next expression
days = month_rem * 30 // 1 #calculate and store days
print()
print(f'Geting older is ruff! As a dog you are {years:.1f} years {months:.1f} months {days:.1f} days old!')
print()

ani_age2 = hum_age / 9  #store age
years = ani_age2 // 1 #calculate and store new age  
yr_rem = ani_age2 % 1 #store remainder for next calculation
months = yr_rem * 12 // 1 #calculate and store months
month_rem = yr_rem * 12 % 1 #calculate and store remainder for next expression
days = month_rem * 30 // 1 #calculate and store days
print(f'As a cat thanks to your 9 lives, you are {years:.1f} years {months:.1f} months {days:.1f} days old!')
print()

ani_age3 = 3*(((((hum_age)** 2) -47) /7) + 12)  #store age
years = ani_age3 // 1 #calculate and store new age  
yr_rem = ani_age3 % 1 #store remainder for next calculation
months = yr_rem * 12 // 1 #calculate and store months
month_rem = yr_rem * 12 % 1 #calculate and store remainder for next expression
days = month_rem * 30 // 1 #calculate and store days
print(f'Hay there, as a horse you are {years:.1f} years {months:.1f} months {days:.1f} days old!')
print()
print('Try again to see how your age changes!')

