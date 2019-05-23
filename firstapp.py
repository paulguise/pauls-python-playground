#boolean values hvae to be capitalized, True and False. lower case wont work

#------ Receiving Input -------
#name = input('What is your name yo glorious bastard? ')
#color = input('And what color do you like ' + name + '? ')
#print('Got it. ' +name+ ' likes '+color+'!')

#------ Variables -------
#birth_year = input('What is your birth year: ')
#print(type(birth_year))
#age = 2019 - int(birth_year)
#print(type(age))
#print(age)
#int() #converts string into an integer
#float() #converts the string into a floating decimal value
#bool() #converts the string ito a boolean value
#type() #will give the type of variable it is
#str() # will convert the value to a string to use when printing in concantenated ways 
#input values from input() are always strings

#------ Type Conversion -------
#the_weight = input('What is your weight in lbs.? ')
#final_weight = int(the_weight) * 0.45
#print('Your weight in kG is ' + str(final_weight))

#------ Strings -------
#course = 'Python for beginners'
#another = course[:] #just clones the variable
#print(another) #the variable can be treated as an array and called as such. can also supply negative values and ranges of values
#name = 'Jennifer'
#print(name[1:-1])

#------ Formatted Strings -------
#useful for generating dynamic text with variables
#first = 'Paul'
#last = 'Guise'
#message = first + ' [' + last + '] is a coder'
#msg = f'{first} [{last}] is a coder' # "f" is a function call for formatted string, curly braces define holes in a string where varibals go
#print(msg)


#------ String Methods -------
#course = 'Python for beginners'
#len() - length of string, number of items in a list
#when a function belongs to somethignn else, or is specific to a type of object, that function is called a method

#print(course.upper())  #called via [object].method()
#print(course.lower()) #string is not changed, but duplicated and then chagned, original is stil intact
#print(course)
#print(course.find('beg')) #will return the index of the first occurence of that character, case sensitive, -1 means not found
#print(course.replace('beginners','Absolute Beginners')) #case sensitive, will not replace if not found, 3rd parameter is # of instances to replace
#print(course.replace('n','O',2))
#print('Python' in course) #boolean expression returned, case sensitive


#------ Arithmeetic Operations -------
#print(10 + 3)
#print(10 * 3)
#print(10 - 3)
#print(10 / 3) #returns normal float of division
#print(10 // 3) #returns integer of division (no remainder)
#print(10 % 3) #modulus, returns the remainder of the devision
#print(10 ** 3) #exponent, power of

#x=10
#x = x + 3
#x += 3 #same as .= in php, augmented assignment operator, increment a number by the integer/float
#x -= 3
#print(x)

#x = 10 + 3 * 2 #follows basic math orders of operation
#print(x)
#parenthesis - always takes priority, left to right
#exonentation
#multiplication or division (in order from left to right)
#addition or subtraction (in order from left to right)

#x = 10 + 3 * 2 ** 2
#print(x)

#x = ( 2 + 3 ) * 10 - 3
#print(x)


#------ Math Functions -------
#is you want to do complext mathematical function, inport the math module 
#https://docs.python.org/3.4/library/math.html
#import math
#x = 2.9
#print(round(x)) #rounds up or down
#print(abs(-2.9)) #absolute always retusn a positive number
#print(math.ceil(2.9))
#print(math.floor(2.9))

#-------- If Statements -------------
#example of psuedo coding 

#    if its hot
#        its a hor dynamic   drink plenty of water
#    otherwise if its cold
#        its a cold day
#        wear warm clothes
#    otherwise  
#         its a lovely day

#is_hot = False
#is_cold = False
#
#if is_hot:
#    print("It's hot outside.")
#    print("Drink plenty of water.")
#elif is_cold:
#    print("It's a cold day")
#    print("Wear warm clothes.")
#else:
#    print("It's a lovely day.")
#print("Enjoy your day.") #not tabbed/indented statement will end an IF statement


#good_credit = False
#house_price = 1000000
#if good_credit:
#    down_payment = house_price * 0.10
#else:
#    down_payment = house_price * 0.20
#
#print(f"Your down payment is $" + format(down_payment,",.2f") + " dollars.")