#Day 3 Exercises - Operators
import math

#Variable Declaration
age = int(26)
height = float(5.833)
complex_number = 1+1j

#triangle area calculator
print("First, we will calculate a triangle's area.")
height = float(input('Enter triangle height: '))
base = float(input('Enter triangle length: '))
area = 0.5 * height * base
print(area)

#triangle perimeter calculator
print('Next, we are going to calculate the perimeter.')
side_1 = float(input('Enter side a: '))
side_2 = float(input('Enter side b: '))
side_3 = float(input('Enter side c: '))
print("The perimeter of the triangle is: " + str(side_1+side_2+side_3))

#rectangle perimeter and area calculator
print('Next, we are going to find the perimeter and area of a square.')
rectangle_side_1 = float(input('Enter the first length: '))
rectangle_side_2 = float(input('Enter the second length: '))
print("The perimeter of a square with given lengths is: " +
      str(2*(rectangle_side_1 + rectangle_side_2)))
print("The area of a rectangle with given lengths is " +
      str(rectangle_side_1 * rectangle_side_2))

#circle area and circumference calculator
print('Next, we are going to do the same for a circle.')
circle_radius = float(input("Enter the radius: "))
print("The area of the circle is " + str(math.pi *(circle_radius ** 2)))
print("The circumference of the circle is " + str(math.pi * 2 * circle_radius))

#Slope, x-intercept, y-intercept of y = 2x-2
y_intercept = -2
x_intercept = 1
slope = 2

#slope + euclid (2,2) and (6,10)
x1,y1, x2, y2 = 2,2,6,10
slope_2 = ((y2-y1)/(x2-x1))
euclid = (math.sqrt(((x2-x1)**2) + ((y2-y1)**2)))
print(slope_2,euclid)
print(slope_2 == slope)

#step 11 skipped -

#step 12-17 - intentionally make false statement with lengths of python and dragon
string_1 = "python"
string_2 = "dragon"
print("under this is lengths comparison")
print(float(len(string_1)) == int(len(string_2)))

'''
skipping this section because it feels very suboptimal to do without if statements,
which aren't covered under this section of the course.

print("under this is checking for on")
print("on" in string_1 and string_2)
'''
string_3 = "I hope this course is not full of jargon."
print("under this is checking for jargon")
print("jargon" in string_3)

print("under this is dragon")
print(str(float(len(string_1))))

#step 18-20
floorer = 7//3
print(floorer == int(2.7))
print(type("10")==type(10))
print(int(float("9.8"))==10)







