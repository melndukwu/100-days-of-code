from logo import logo

def add(n1,n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

while True:
    print(logo)
    num1 = float(input("What's the first number?: "))
    op = input("Choose an operation: + - * / \n")
    num2 = float(input("What's the next number?: "))

    result = (operations[op](num1, num2))
    print(f"{num1} {op} {num2} = {result}")

    should_continue = True

    while should_continue:
        answer = input("Do you want to continue working with the previous result? Type 'yes' or 'no'. ").lower()

        if answer == "yes":
            op = input("Choose an operation: + - * / \n")
            num2 = float(input("What's the next number?: "))
            result_before = result
            result = operations[op](result, num2)
            print(f"{result_before} {op} {num2} = {result}")

        elif answer == "no":
            should_continue = False
            print("\n" * 25)
