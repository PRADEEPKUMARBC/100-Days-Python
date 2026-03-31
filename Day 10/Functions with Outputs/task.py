def format_name(f_name, l_name ):
    print(f_name.title())
    print(l_name.title())

format_name(f_name="angela", l_name="AngeLa")

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)

