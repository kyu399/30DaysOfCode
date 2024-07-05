# Variables List
#Exercise Level 1
first_name = 'Kevin'
last_name = 'Yu'
full_name = first_name + " " + last_name
country = 'USA'
city = 'Around Daly City'
age = 26
is_married = False
year = 2024 - age
is_true = True
is_light_on = True
first_name_2, last_name_2 = 'Tester','Two'

#Exercise Level 2 - Type Checking
import math #imported math library for pi value 
print(type(first_name))
'''
Omitted checking the types of all the other variables.
I am familiar with the command and we will not be using
the types in other spots later.
'''

print("My first name is" + " " + str(len(first_name)-len(last_name))
       + " " + "letters longer than my last name.")

num_one = 5
num_two = 4
sum = num_one + num_two
diff = num_one - num_two
multip = num_one * num_two
divis = num_one / num_two
modu = num_two % num_one
pwr = num_one ** num_two
flr = num_one // num_two

circle_radius = 30
area_of_circle = math.pi * (circle_radius**2)
circum_of_circle = 2 * math.pi * circle_radius
print(area_of_circle)
print(circum_of_circle)

f_n_input = input('What is your name?')
l_n_input = input('What is your last name?')
country_input = input('What country are you from?')
age_input = input('How old are you in years?')
print(f_n_input,l_n_input,country_input,age_input)

