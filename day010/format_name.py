def format_name(f_name, l_name):
    return f"{f_name.title()} {l_name.title()}" 

f_name = input("First name: ")
l_name = input("Last name: ")
print(format_name(f_name, l_name))