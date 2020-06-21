import re
from mlexer import *
from utils import *

lex = Lexer()

def priority(c):
    if c == '^':
        return 4
    elif c == '*' or c == '/':
        return 3
    elif c == '+' or c == '-':
        return 2
    elif c in lex.argOperators:
        return 1
    return 0

exp = input()
res = None
stk = []
i = 0
while i < len(exp):
    cur = exp[i]
    if isBelongToIdentifier(cur) or checkDigit(cur):
        idx = i + 1
        while idx < len(exp) and (lex.checkValidIndentifier(cur+exp[idx]) or lex.checkValidInteger(cur+exp[idx]) or lex.checkValidFloat(cur+exp[idx])):
            cur += exp[idx]
            idx += 1
        i = idx
    elif cur == '(':
        stk.append((cur, i))
        i += 1
    elif cur == ')':
        while len(stk) > 0 and stk[-1][0] != '(':
            res = stk.pop(-1)
        stk.pop(-1)
        i += 1
    elif cur in lex.argOperators:
        idx = i + 1
        while idx < len(exp) and (cur+exp[idx]) in lex.argOperators:
            cur += exp[idx]
            idx += 1
        while len(stk) > 0 and priority(stk[-1][0]) >= priority(cur):
            res = stk.pop(-1)
        stk.append((cur, i))
        i = idx
    else:
        i += 1
while len(stk) > 0:
    res = stk.pop(-1)
print(res)