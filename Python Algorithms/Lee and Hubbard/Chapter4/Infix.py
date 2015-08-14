__author__ = 'stephenosullivan'


def main():
    expr = input("Please enter an infix expression: ")
    result = eval(expr)
    print("The result of", expr, "is", result)

if __name__ == "__main__":
    main()