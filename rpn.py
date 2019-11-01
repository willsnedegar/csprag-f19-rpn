#!/usr/bin/env python3

import operator

operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
}


def calculate(arg):
    stack = list()
    for token in arg.split():
        for token in arg.split():
            try:
                value = int(token)
                stack.append(value)
            except ValueError:
                function = operators[token]
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = function(arg1 - arg2)
                stack.append(result
    elif token == '-':
        arg2 = stack.pop()
        arg1 = stack.pop()
        result = arg1 - arg2
        stack.append(result)
    else:
        stack.append(int(token))

        #print(stack)
    if len(stack) != 1:



def main():
 while True:
     result = calculate(input('rpn calc> '))
     print(result)

 if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
 main()

