def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name. """
    if f_name == '' or l_name == '':
        return "You didn't provide valid inputs."
    
    return f"{f_name.title()} {l_name.title()}" 


# f_name = input("First name: ")
# l_name = input("Last name: ")
print(format_name(input("First name: "), input('Last name: ')))

format_name()