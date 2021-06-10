'''William Martell Project 4: Stacks'''
from stack import Stack

def main():
    '''Turns an infix expression into a postfix expression'''
    s_stack = Stack()
    with open("data.txt") as data:
        for infix_expression in data:
            for variable in infix_expression:
                s_stack.push(variable)
            print("infix: " + infix_expression)
            postfix = in2post(infix_expression)
            print("postfix: " + str(postfix))
            evaluation = eval_postfix(postfix)
            print("answer: " + str(evaluation) +'\n')

def in2post(infix):
    '''Checks if the infix expression is valid and then turns it into a postfix string'''
    if type(infix) != str:
        raise ValueError("The infix expression must be a string.")
    left = 0
    right = 0
    for value in infix:
        if isLeftParenthesis(value):
            left += 1
        elif isRightParenthesis(value):
            right += 1
    if left != right:
        raise SyntaxError("You entered an invalid expression.")

    operator_stack = Stack()
    postfix_expr = ''
    for value in infix:
        if value == '0':
            postfix_expr += value
        elif value == '1':
            postfix_expr += value
        elif value == '2':
            postfix_expr += value
        elif value == '3':
            postfix_expr += value
        elif value == '4':
            postfix_expr += value
        elif value == '5':
            postfix_expr += value
        elif value == '6':
            postfix_expr += value
        elif value == '7':
            postfix_expr += value
        elif value == '8':
            postfix_expr += value
        elif value == '9':
            postfix_expr += value
        else:
            if isLeftParenthesis(value):
                operator_stack.push(value)
            elif isRightParenthesis(value):
                operator = operator_stack.pop()
                while not isLeftParenthesis(operator):
                    postfix_expr += operator
                    operator = operator_stack.pop()
            else:
                while (not operator_stack.is_empty()) and hasLessOrEqualPriority(value, operator_stack.top()):
                    postfix_expr += operator_stack.pop()
                operator_stack.push(value)

    while not operator_stack.is_empty():
        postfix_expr += operator_stack.pop()

    return postfix_expr

def hasLessOrEqualPriority(value, stack_operator):
    '''Checks if the operator in the stack has less or equal priority'''
    priority = 0
    value_priority = 0
    if stack_operator == "*":
        priority = 2
    elif stack_operator == "/":
        priority = 2
    elif stack_operator == "+":
        priority = 1
    elif stack_operator == "-":
        priority = 1

    if value == '*':
        value_priority = 2
    elif value == '/':
        value_priority = 2
    elif value == "+":
        value_priority = 1
    elif value == "-":
        value_priority = 1

    if value_priority > priority:
        return False

    return True

def isLeftParenthesis(value):
    '''Checks if the value given is a left parenthesis'''
    if value != '(':
        return False
    return True

def isRightParenthesis(value):
    '''Checks if the value give is a right parenthesis'''
    if value != ')':
        return False
    return True

def eval_postfix(postfix):
    '''Performs the arithmetic on the postfix expression, returning the resulting value'''
    if type(postfix) != str:
        raise ValueError("You have entered an invalid expression.")
    counter = 0
    for value in postfix:
        if value == '0':
            counter += 1
        elif value == '1':
            counter += 1
        elif value == '2':
            counter += 1
        elif value == '3':
            counter += 1
        elif value == '4':
            counter += 1
        elif value == '5':
            counter += 1
        elif value == '6':
            counter += 1
        elif value == '7':
            counter += 1
        elif value == '8':
            counter += 1
        elif value == '9':
            counter += 1
        elif value == '+':
            counter -= 1
        elif value == '-':
            counter -= 1
        elif value == '*':
            counter -= 1
        elif value == '/':
            counter -= 1
    if counter == 0:
        raise SyntaxError("Expression must be valid.")

    evaluation_stack = Stack()
    for value in postfix:
        if value == '0':
            evaluation_stack.push(0)
        elif value == '1':
            evaluation_stack.push(1)
        elif value == '2':
            evaluation_stack.push(2)
        elif value == '3':
            evaluation_stack.push(3)
        elif value == '4':
            evaluation_stack.push(4)
        elif value == '5':
            evaluation_stack.push(5)
        elif value == '6':
            evaluation_stack.push(6)
        elif value == '7':
            evaluation_stack.push(7)
        elif value == '8':
            evaluation_stack.push(8)
        elif value == '9':
            evaluation_stack.push(9)
        elif value == '+':
            value_2 = evaluation_stack.pop()
            value_1 = evaluation_stack.pop()
            evaluation_stack.push(float(value_1 + value_2))
        elif value == '-':
            value_2 = evaluation_stack.pop()
            value_1 = evaluation_stack.pop()
            evaluation_stack.push(float(value_1 - value_2))
        elif value == '*':
            value_2 = evaluation_stack.pop()
            value_1 = evaluation_stack.pop()
            evaluation_stack.push(float(value_1 * value_2))
        elif value == '/':
            value_2 = evaluation_stack.pop()
            value_1 = evaluation_stack.pop()
            evaluation_stack.push(float(value_1 // value_2))

    result = evaluation_stack.pop()
    return float(result)

if __name__ == "__main__":
    main()
