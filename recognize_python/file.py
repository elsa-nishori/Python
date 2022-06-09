num1 = 42 # variable declaration, initialize numbers(integers)
num2 = 2.3 # variable declaration, initialize numbers(decimals)
boolean = True # variable declaration, initialize boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # declaring and initializing a list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # declaring and initializing a dictionary
fruit = ('blueberry', 'strawberry', 'banana') # declaring and initializing a tuple
print(type(fruit)) # log statement, type check
print(pizza_toppings[1]) # log statement, access list value
pizza_toppings.append('Mushrooms') # add value to the list
print(person['name']) # log statement, access dictionary value
person['name'] = 'George' # change dictionary value
person['eye_color'] = 'blue' # add value to the dictionary
print(fruit[2]) # log statement, access tuple value

# conditionals, log statements
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# for loops, log statements
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

# deleting list values
pizza_toppings.pop()
pizza_toppings.pop(1)

print(person) # log statement
person.pop('eye_color') # delete value
print(person) # log statement

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #conditional
        continue
    print('After 1st if statement') # log statement
    if topping == 'Olives': #conditional
        break

def print_hello_ten_times(): # function
    for num in range(10): # for loop
        print('Hello') # log statement

print_hello_ten_times() # function call

def print_hello_x_times(x): # function with one parameter
    for num in range(x): # for loop
        print('Hello') # log statement

print_hello_x_times(4) # function call

def print_hello_x_or_ten_times(x = 10): # function definition with one optional parameter
    for num in range(x): # for loop
        print('Hello') # log statement

print_hello_x_or_ten_times() # function call with default parameter value
print_hello_x_or_ten_times(4) # function call with new parameter value


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)