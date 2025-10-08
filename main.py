from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1- n2
def multiply(n1, n2):
    return n1* n2
def divide (n1, n2):
    return n1/n2
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
def calculator():
     should_continue = True
     n1 = float(input("Type the first number"))
     while should_continue:
        for symbal in operations:
            print(symbal)
        operation_symbal = input(f"Type the mathematical operator",)
        n2 = float(input("Type the next number"))
        answer = operations[operation_symbal](n1, n2)
        print(f"{n1} {operation_symbal} {n2} = {answer}")
        choice = input("do you want to continue working type 'y' or you want a new calculator type 'n'").lower()
        if choice =="y":
            n1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()
calculator()

