# calculator
# addition
def add(n1, n2):
    return n1 + n2

# subtraction


def sub(n1, n2):
    return n1 - n2

# multipy


def multi(n1, n2):
    return n1 * n2

# division


def divide(n1, n2):
    return n1 / n2


operation = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": divide
}


def calculator():
    num1 = float(input("what is the  number?"))
    should_continue = True
    while should_continue:
        for symbol in operation:
            print(symbol)
        operation_symbol = input("pick an operation from the line above:")
        num2 = float(input("what is second number?"))

        answer = operation[operation_symbol]
        x = answer(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {x}")
        calagain = input(
            f"type 'y' to continue calculating with {x}, or type 'n' to exit.: ")
        if calagain == "y":
            num1 = x
        else:
            should_continue = False
            calculator()


calculator()
