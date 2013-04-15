#!/usr/bin/env python
# Support numbers , () and +-*/, they must be separated by space
from stack import Stack

# infix -> postfix
# 1. Create a opstack for keeping operators, create a list for output
# 2. Split input infix expression by space
# 3. Scan the token list:
#    * operand: append to output list
#    * (: push to opstack
#    * ): pop from opstack util a ( is poped, append them to output list
#    * +-*/: push to opstack, but first remove operators from opstack whose 
#            precedence is equal or higher and append them to output list
# 4. If opstack is not empty, pop and then append them to output list 
def infixToPostfix(infixexpr):
    prec = {'+':2, '-':2, '(':1, ')':1, '*':3, '/':3, '^':10}
    opstack = Stack()
    postfixList = []
    infixList = infixexpr.split()

    for sym in infixList:
        if sym == '(':
            opstack.push(sym)
        elif sym == ')':
            topSym = opstack.pop()
            while topSym!='(':
                postfixList.append(topSym)
                topSym = opstack.pop()
        elif sym in '+-*/^':
            while (not opstack.isEmpty()) and prec[opstack.peek()]>=prec[sym]:
                postfixList.append(opstack.pop())
            opstack.push(sym)
        else:
            postfixList.append(sym)
    while not opstack.isEmpty():
        postfixList.append(opstack.pop())

    return ' '.join(postfixList)

def cacPostfixExpr(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token.isdigit():
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            operandStack.push(doMath(operand1, operand2, token))
    return operandStack.pop()

def doMath(op1, op2, op):
    if op=='+':
        return op1+op2
    elif op=='-':
        return op1-op2
    elif op=='*':
        return op1*op2
    elif op=='/':
        return op1/op2

if __name__=='__main__':
    print infixToPostfix('A * B + C * D')
    print infixToPostfix('( A + B ) * C - ( D - E ) * ( F + G )')
    print infixToPostfix('10 + 3 * 5 / ( 16 - 4 )')
    print cacPostfixExpr(infixToPostfix('10 + 3 * 5 / ( 16 - 4 )'))
    print cacPostfixExpr('17 10 + 3 * 9 /')
    print infixToPostfix('5 * 3 ^ ( 4 - 2 )')
