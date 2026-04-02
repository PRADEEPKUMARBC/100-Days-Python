a = 1
def my_function():
    a += 1
    print(a)
my_function()

a = 1
def my_function():
    global a
    a += 1
    print(a)

my_function()