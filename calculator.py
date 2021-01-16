# Program: Calculator
# Name: Gurtej Virdi
# Date: Oct 25, 2020

# How does it help?
# It makes the act of calculating effortless
# Where one may take a lot of time to solve numbers involving operations this would make the task quicker

# Print program name
def introduction():
    print('Python Calculator')


# Print instructions
def instructions():
    print('Type the calculation in this format: 1+2\nPossible operations: +, -, *, /')


# Get user input
def get_user_input():
    return input('Enter calculation: ').replace(' ', '')


# Calculate user input
def calculate(s):
    try:
        return float(s)
    except ValueError:
        pass
    if '+' in s:
        return add(calculate(s.split('+', maxsplit=1)[0]), calculate(s.split('+', maxsplit=1)[1]))
    elif '-' in s:
        return subtract(calculate(s.split('-', maxsplit=1)[0]), calculate(s.split('-', maxsplit=1)[1]))
    elif '*' in s:
        return multiply(calculate(s.split('*', maxsplit=1)[0]), calculate(s.split('*', maxsplit=1)[1]))
    elif '/' in s:
        return divide(calculate(s.split('/', maxsplit=1)[0]), calculate(s.split('/', maxsplit=1)[1]))


# Add two numbers
def add(x, y):
    return x + y


# Subtract two numbers
def subtract(x, y):
    return x - y


# Multiply two numbers
def multiply(x, y):
    return x * y


# Divide two numbers
def divide(x, y):
    return x / y


# String output
def answer_user(out):
    return 'Answer: ' + str(out)


# Save output
def write_to_file(calc, out):
    f = open('output.txt', 'a')
    f.write(calc + '=' + str(out) + '\n')
    f.close()


# Ask to run again
def ask_again():
    return input('Do you want to enter another calculation? ')[0].lower() == 'y'


# Main
def main():
    open('output.txt', 'w').close()
    introduction()
    print()
    instructions()
    while True:
        print()
        calc = get_user_input()
        out = calculate(calc)
        print(answer_user(out))
        write_to_file(calc, out)
        print()
        if not ask_again():
            print()
            print('Thank you for using the program!\nGood Bye!')
            exit()


if __name__ == '__main__':
    main()
