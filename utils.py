def checkLetter(c):
        num = ord(c)
        return (num > 64 and num < 91) or (num > 96 and num < 123) or num == 95

def checkDigit(c):
    num = ord(c)
    return num > 47 and num < 58

def checkNumberOneToSeven(c):
	return ord(c) > 48 and ord(c) < 56

def checkPositiveNumber(c):
	return ord(c) > 48 and ord(c) < 58

def isOperator(c):
    return c == '+' or c =='-' or c =='*' or c == '/'

def isBracket(c):
    return c == '(' or c == ')'

def isSpace(c):
    return c == ' '

def printAST(res, depth):
    if isinstance(res, str):
        ident = ' ' * depth
        print(ident + res)
        return
    for i in range(len(res)):
        printAST(res[i], depth+1)
    
def countHeadTabs(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == '\t':
            cnt += 1
    return cnt

def isBelongToIdentifier(c):
    return c == '$' or c == '@' or (ord(c) >= ord('a') and ord(c) <= ord('z'))

def print_list(lst, level=0):
    # if level > 0:
    #     print('  ' * level + '|')
    for e in lst:
        if isinstance(e, list):
            print_list(e, level + 1)
        else:
            print('  ' * level + e)