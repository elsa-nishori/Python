# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]["last_name"] = "Bryant"
print(students)

sports_directory["soccer"][0] = "Andres"
print(sports_directory)

z[0]["y"] = 30
print(z)

# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.
def iterateDictionary(some_list):
    for i in range(len(some_list)):
        for key, val in some_list[i].items():
            if key != list(some_list[i].keys())[-1]:
                print(f"{key} - {val}", end=', ')
            else:
                print(f"{key} - {val}")

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
iterateDictionary(students) 

# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        for key, val in some_list[i].items():
            if key == key_name:
                print(val)

iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)
print("--------------------------------")

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list.
def printInfo(some_dict):
    for key, val in some_dict.items():
        print(f"{len(some_dict[key])} {key.upper()}")
        for item in val:
            print(item)
        print("-------------------------------")

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

# Two other ways for implementing the 4th task

# def printInfo(some_dict):
#     for each_key in some_dict:
#         print(f"{len(some_dict[each_key])} {each_key.upper()}")
#         for i in range(len(some_dict[each_key])):
#             print(some_dict[each_key][i])

# def printInfo(some_dict):
#     for key in some_dict.keys():
#         print(f"{len(some_dict[key])} {key.upper()}")
#         for val in some_dict[key]:
#             print(val)
