
print("Hello , Python World") #print function is use to print hello python world


''' 
Name=(input("enter your frist name "))
lastName=(input("enter your last name"))
print(Name[::-1]+" "+ lastName[::-1]) 
'''

'''
String_1 = "QWERT Keyboards"
String_2 = "methods"
print(String_2.capitalize()) # Capitalize frist letter of the String
print(String_1.lower()) # converts all the characters to lower case
'''

'''
Number=int(input("Enter a number "))
print(int(Number)) # converts to integer
print(float(Number)) # converts to floating point
print(complex(Number)) # converts to complex form i.e a + bj
'''

'''
leng = int(input("Enter length of Rectangle"))
wid = int(input("Enter width of Rectangle"))
Area = leng * wid
print("Area of Rectangle is :" , Area)


print("Area of Rectangle is{:.2f}".format(Area)) # using format func the area is converted to float with 2 decimal

'''

'''
num_1 = int(input("Enter frist number"))
num_2 = int(input("Enter second number"))
num_3 = int(input("Enter third number"))
Avg = (num_1+num_2+num_3)/3
print("Average of three numbers enteres by you is %d" % Avg) # here we have used String formating method where we use
                                                             # % to insert the Avg in the String
print("The average of three numbers is:" , [float((num_1+num_2+num_3)/3)])
'''
#PART3
'''
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")
'''
'''
while True:
    user_input = input("Enter a number (or type 'exit' to stop): ")

    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break  # Exit the loop if the user types "exit"
'''
'''
while True:
    user_input = input("Enter a number (or type 'exit' to stop): ")

    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break  # Exit the loop if the user types "exit"
    else:
        continue  # this will ask the user for the input 

'''
'''
# Input: Ask the user for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Logic: Use relational and logical operators to determine the type of numbers
if num1 % 2 == 0 and num2 % 2 == 0:
    print(f"Both {num1} and {num2} are even.")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print(f"Both {num1} and {num2} are odd.")
else:
    print(f"One number is odd and the other is even.")
'''
