# Simple Calculator in pyhton

#Add the number
def addition(number1,number2):
    return (number1+number2)

#Substract the number
def substraction(number1,number2):
    return (number1-number2)

#Multiply the number
def multiply(number1,number2):
    return (number1*number2)

#Divide the number
def division(number1,number2):
    if number2 == 0 :
        print("You Entered Invalid Number")
    else:
        return (number1/number2)

#create dictionary of the operations

operations ={"+":addition,
             "-":substraction,
             "*":multiply,
             "/":division}


def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()

