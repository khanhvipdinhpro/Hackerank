"1. Python string format() function"
print("1. Python string format() function")
#string format
txt = "I have {an:.2f} Ruppes!\n"
print(txt.format(an = 4))


"2. Using a Single Formatter"
print("2. Using a Single Formatter")
# using format option in a simple string
print("{}, A computer science portal for geeks."
      .format("GeeksforGeeks"))
# using format option for a
# value stored in a variable
str = "This article is written in {}"
print(str.format("Python"))
# formatting a string using a numeric constant
print("Hello, I am {} years old !\n".format(18))


"3. String format() with multiple placeholders"
print("3. String format() with multiple placeholders")
# Multiple placeholders in format() function
my_string = "{}, is a {} science portal for {}"
print(my_string.format("GeeksforGeeks", "computer", "geeks"))
# different datatypes can be used in formatting
print("Hi ! My name is {} and I am {} years old"
      .format("User", 19))
# The values passed as parameters
# are replaced in order of their entry
print("This is {} {} {} {}\n"
      .format("one", "two", "three", "four"))


#String format() IndexError
# parameters in format function.OUT OF RANGE
#my_string = "{}, is a {} {} science portal for {}"
#print(my_string.format("GeeksforGeeks", "computer", "geeks"))


#Formatters with Positional and Keyword Arguments
# Positional arguments
# are placed in order
print("{0} love {1}!!".format("GeeksforGeeks",
                              "Geeks"))
# Reverse the index numbers with the
# parameters of the placeholders
print("{1} love {0}!!".format("GeeksforGeeks",
                              "Geeks"))
print("Every {} should know the use of {} {} programming and {}"
      .format("programmer", "Open", "Source",
              "Operating Systems"))
# Use the index numbers of the
# values to change the order that
# they appear in the string
print("Every {3} should know the use of {2} {1} programming and {0}"
      .format("programmer", "Open", "Source", "Operating Systems"))
# Keyword arguments are called
# by their keyword name
print("{gfg} is a {0} science portal for {1}\n"
      .format("computer", "geeks", gfg="GeeksforGeeks\n"))


#Using %s – string conversion via str() prior to formatting
print("%20s" % ('geeksforgeeks', ))
print("%-20s" % ('Interngeeks', ))
print("%.5s" % ('Interngeeks', ))


#Using %c– character  prior to formatting
type = 'bug'
result = 'troubling'
print('I wondered why the program was %s me. Then\
it dawned on me it was a %s .\n' %
      (result, type))


#Using %i signed decimal integer and %d signed decimal integer(base-10) prior to formatting
match = 12000
site = 'amazon'
print("%s is so useful. I tried to look\
up mobile and they had a nice one that cost %d rupees.\n" % (site, match))


#Convert base-10 decimal integers to floating-point numeric constants 
print("This site is {0:f}% securely {1}!!".
      format(100, "encrypted"))
# To limit the precision
print("My average of this {0} was {1:.2f}%"
      .format("semester", 78.234876))
# For no decimal places
print("My average of this {0} was {1:.0f}%"
      .format("semester", 78.234876))
# Convert an integer to its binary or
# with other different converted bases.
print("The {0} of 100 is {1:b}"
      .format("binary", 100))
print("The {0} of 100 is {1:o}\n"
      .format("octal", 100))


#Type Specifying Errors
# When explicitly converted floating-point
# values to decimal with base-10 by 'd'
# type conversion we encounter Value-Error.
#print("The temperature today is {0:d} degrees outside !".format(35.567))
 
# Instead write this to avoid value-errors
''' print("The temperature today is {0:.0f} degrees outside !"
                                            .format(35.567))'''

        
#Padding Substitutions or Generating Spaces
# To demonstrate spacing when
# strings are passed as parameters
print("{0:4}, is the computer science portal for {1:8}!"
      .format("GeeksforGeeks", "geeks"))
# To demonstrate spacing when numeric
# constants are passed as parameters.
print("It is {0:5} degrees outside !"
      .format(40))
# To demonstrate both string and numeric
# constants passed as parameters
print("{0:4} was founded in {1:16}!"
      .format("GeeksforGeeks", 2009))
# To demonstrate aligning of spaces
print("{0:^16} was founded in {1:<10}!"
      .format("GeeksforGeeks", 2009))
print("{:*^20s}\n".format("Geeks"))


#Applications
# which prints out i, i ^ 2, i ^ 3,
#  i ^ 4 in the given range
# Function prints out values
# in an unorganized manner
def unorganized(a, b):
    for i in range(a, b):
        print(i, i**2, i**3, i**4)
# Function prints the organized set of values
def organized(a, b):
    for i in range(a, b):
 
        # Using formatters to give 6
        # spaces to each set of values
        print("{:6d} {:6d} {:6d} {:6d}"
              .format(i, i ** 2, i ** 3, i ** 4))
# Driver Code
n1 = int(3)
n2 = int(10)
print("------Before Using Formatters-------")
# Calling function without formatters
unorganized(n1, n2)
print()
print("-------After Using Formatters---------")
print()
# Calling function that contains
# formatters to organize the data
organized(n1, n2)


#Using a dictionary for string formatting
introduction = 'My name is {first_name} {middle_name} {last_name} AKA the {aka}.\n'
full_name = {
    'first_name': 'Tony',
    'middle_name': 'Howard',
    'last_name': 'Stark',
    'aka': 'Iron Man',
}
# Notice the use of "**" operator to unpack the values.
print(introduction.format(**full_name))


#Python format() with list
# Python code to truncate float
# values to 2 decimal digits.
# List initialization
Input = [100.7689454, 17.232999, 60.98867, 300.83748789]
# Using format
Output = ['{:.2f}'.format(elem) for elem in Input]
# Print output
print(Output)