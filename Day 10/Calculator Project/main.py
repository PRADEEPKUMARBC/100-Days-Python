import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiple(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

dictionary_values = {}

operations = {
    "+": add,
    "-": subtract,
    "*": multiple,
    "/": divide
}

# TODO = Use the dictionary operations to perform the calculations . multiply 4 * 8 using dictionary

def calculator():
    print(art.logo)
    should_accumulate = True
    first_num = float(input("Enter the first number: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        type_math_oper = input("Pick an operations : ")
        second_num = float(input("Enter the second number: "))
        answer = operations[type_math_oper](first_num, second_num)
        print(f"{first_num} {type_math_oper} {second_num} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to stop: ")

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("/n" * 20)

calculator()