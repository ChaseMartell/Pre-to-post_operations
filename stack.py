'''William Martell Project 4: Stacks'''

class Stack():
    '''Implements a stack data structure'''
    def __init__(self):
        self.stack = []

    def push(self,value):
        '''adds value to the top of the stack'''
        self.stack.append(value)

    def pop(self):
        '''removes the top value off of the stack'''
        if len(self.stack) == 0:
            raise IndexError("Stack is empty")
        return self.stack.pop()

    def top(self):
        '''returns the top value on the stack, without removing it'''
        if len(self.stack) == 0:
            raise IndexError("Stack is empty")
        return self.stack[len(self.stack) - 1]

    def is_empty(self):
        '''Returns true if the stack is empty, false if not'''
        return len(self.stack) == 0

    def clear(self):
        '''Empties the stack'''
        self.stack = []

    def size(self):
        '''Returns the size of the stack'''
        return len(self.stack)

    def __str__(self):
        '''Produces a string format of the stack'''
        string = ""
        for val in self.stack:
            string += (str(val) + " ")
        return string
