import art

def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}

def calculator():
    print(art.logo)
    num1 = float(input("what is the first number: "))
    should_accumulate = True
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operations_symbol = input('Pick an operation: ')
        num2 = float(input("what's the next number: "))
        answer = operations[operations_symbol](num1, num2)
        print(f"{num1} {operations_symbol} {num2} = {answer}")
        choice = input(f"Type 'y' to continue calcalating with {answer}, or type 'n' to start new calculation: ".lower())
        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()
            
calculator()