programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again."
}

# # Retrive items from dict
# print(programming_dictionary['Bug'])

# # Add new items to dict
programming_dictionary['Loop'] = 'The action of doing something over and over again.'
# print(programming_dictionary)

# # Wipe out an existing dict
# empty_dict = {}
# programming_dictionary = empty_dict
# print(programming_dictionary)

# Edit an item in a dict
# programming_dictionary['Bug'] = 'A moth in your program.'
# print(programming_dictionary)

for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

#######################################

#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]