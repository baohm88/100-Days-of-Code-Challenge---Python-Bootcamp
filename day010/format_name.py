def format_name(f_name, l_name):
    if f_name == '' or l_name == '':
        return "You didn't provide valid inputs."
    
    return f"{f_name.title()} {l_name.title()}" 


# f_name = input("First name: ")
# l_name = input("Last name: ")
print(format_name(input("First name: "), input('Last name: ')))

