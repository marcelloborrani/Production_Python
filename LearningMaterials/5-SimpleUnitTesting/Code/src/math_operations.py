def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError('Can\'t divide by 0.')
    else:
        return num1 / num2

if __name__ == "__main__": # aka if you press the run button on this file, only run this code. otherwise, don't run it!!
    print("src.math_operations is being executed directly.")
