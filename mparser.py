import re
from utils import *

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.keywords = ["if", "while", "until", "then", "do", "else", "elsif", "not", "and", "or", "end"]
        self.grammar = {
            "STMT": [
                ("if", r".+ if .+"),
                ("while", r".+ while .+"),
                ("until", r".+ until .+"),
                # ("expr", r".+"),
            ],
            "EXPR": [
                ("and", r"(?!if).+ and .+"),
                ("or", r".+ or .+"),
                ("not", r"not .+"),
                # ("arg", r".+")
            ],
            "PRIMARY": [
                ("while", r'while(.+\n)*end'),
                ("if", r'if (.+\n)+(elsif .+\n)*(else.*\n)?end'),
                ("until", r'until(.+\n)*end')
            ]
        }

    def parseCode(self, code):
        deriveStmtRes = self.deriveStatement(code)
        if deriveStmtRes == None:
            return None
        return [":program", deriveStmtRes]

    
    def getAllKeyWords(self, code):
        pass

    
    def deriveStatement(self, stmt):
        if stmt == '':
            return None
        matchStmt = False
        for rule in self.grammar["STMT"]:
            if re.match(rule[1], stmt):
                matchStmt = True
        if not matchStmt:
            return self.deriveExpression(stmt)
        keywords = self.lexer.getAllKeyWords(stmt, self.lexer.stmtKeywords)
        # for i in range(len(keywords)-1, -1, -1):
        kw = keywords[-1]
        parses = stmt.split(" " + kw[1] + " ")
        leftStmt = self.deriveStatement(parses[0])
        rightExpr = self.deriveStatement(parses[1])
        res = []
        if rightExpr != None:
            res.append(rightExpr)
        if leftStmt != None:
            res.append(leftStmt)
        return [':'+kw[1], res]


    def processStmtRule(self, ruleName):
        pass


    def deriveExpression(self, expr):
        if expr == '':
            return []
        matchExpr = False
        for rule in self.grammar["EXPR"]:
            if re.match(rule[1], expr):
                matchExpr = True
        if not matchExpr:
            return self.deriveArg(expr)
        keywords = self.lexer.getAllKeyWords(expr, self.lexer.exprKeywords)
        # for i in range(len(keywords)-1, -1, -1):
        kw = keywords[-1]
        parses = expr.split(" " + kw[1] + " ")
        leftExpr = self.deriveExpression(parses[0])
        rightExpr = self.deriveExpression(parses[1])
        res = []
        if leftExpr != None:
            res.append(leftExpr)
        if rightExpr != None:
            res.append(rightExpr)
        return ["@binary: " + kw[1], res]


    def deriveArg(self, arg):
        if arg == '':
            return None
        for rule in self.grammar["PRIMARY"]:
            if re.match(rule[1], arg):
                return self.derivePrimary(rule[0], arg)
        splitOp = self.getOperatorToSplit(arg)
        # if arg not match any statement (if, while, until) or compare expression -> derive arg as identifier, variable
        if splitOp == None:
            return self.derivePrimary(None, arg.strip(')').strip('('))
        parses = arg.split(splitOp[0])
        leftArg = self.deriveArg(parses[0])
        rightArg = self.deriveArg(parses[1])
        if leftArg == None or rightArg == None:
            return None
        res = [leftArg, rightArg]
        return ["@op: " + splitOp[0], res]


    def derivePrimary(self, statement, primary):
        if statement != None:
            if statement == "if":
                return self.handleIfPrimary(primary)
            if statement == "while" or statement == "until":
                return self.handleWhileUntilPrimary(statement, primary)
        if primary == '':
            return None
        primary = primary.strip(' ').strip('(').strip(')')
        if self.lexer.checkValidIndentifier(primary):
            return ["@ident: " + primary]
        return self.deriveLiteral(primary)
        
    
    def deriveLiteral(self, lit):
        if lit == '':
            return None
        if self.lexer.checkValidInteger(lit):
            return ["@int: " + lit]
        if self.lexer.checkValidFloat(lit):
            return ["@float: " + lit]
        if len(lit) == 1:
            return None
        if (lit[0] == '"' and lit[-1] == '"') or (lit[0] == '`' and lit[-1] == '`'):
            return ["@str:" + lit]
        return None


    def deriveSymbol(self, symb):
        if self.lexer.checkValidInteger(symb):
            return ["@int: " + symb]
        if self.lexer.checkValidFloat(symb):
            return ["@float: " + symb]
        return ["@op: " + symb]

        
    def handleIfPrimary(self, primary):
        res = []
        lines = [l for l in primary.split('\n') if l != '']
        if len(lines) == 0:
            return None
        # handle line 0 which contains 'if'
        outerIf = []
        currOuter = "if"
        k = 0
        # handle elsif, else
        while k < len(lines)-1:
            if lines[k][0] == '\t':
                innerStmt = lines[k] + '\n'
                startStmtTabCounts = countHeadTabs(innerStmt)
                idx = k + 1
                while idx < len(lines)-1 and lines[idx][0] == '\t' and countHeadTabs(lines[k]) < startStmtTabCounts:
                    innerStmt += lines[idx] + '\n'
                    idx += 1
                k = idx
                innerStmtRes = self.deriveStatement(innerStmt.strip('\t').strip('\n'))
                if innerStmtRes == None:
                    return None
                # if is outer most
                if currOuter == "if":
                    outerIf[-1].append(innerStmtRes)
                else:
                    outerIf[-1][-1].append(innerStmtRes)
            else:
                kws = ["if", "elsif", "else"]
                for kw in kws:
                    if lines[k].find(kw) == 0:
                        tokens = [e for e in lines[k].split(kw) if e != '']
                        if len(tokens) == 0:
                            outerIf.append([":"+kw, []])
                            break
                        exprAndStmt = tokens[0].split('\n')
                        parentExpr = exprAndStmt[0].strip()
                        parentExprRes = self.deriveExpression(parentExpr)
                        if parentExprRes == None:
                            return None
                        if kw == "if":
                            # Blank list reserved for statement derivation
                            outerIf = [":if", parentExprRes, []]
                            currOuter = "if"
                        else:
                            outerIf.append([":"+kw, parentExprRes, []])
                            currOuter = kw
                        break
                k += 1
        res.append(outerIf)
        return res
    

    def handleWhileUntilPrimary(self, kw, primary):
        res = []
        lines = [l for l in primary.split('\n') if l != '']
        if len(lines) == 0:
            return None
        k = 0
        while k < len(lines)-1:
            if lines[k][0] == '\t':
                innerStmt = lines[k] + '\n'
                startStmtTabCounts = countHeadTabs(innerStmt)
                idx = k + 1
                while idx < len(lines) and lines[idx][0] == '\t' and countHeadTabs(lines[k]) < startStmtTabCounts:
                    innerStmt += lines[idx] + '\n'
                    idx += 1
                k = idx
                innerStmtRes = self.deriveStatement(innerStmt.strip('\t').strip('\n'))
                if innerStmtRes == None:
                    return None
                res[-1].append(innerStmtRes)
            else:
                tokens = [e for e in lines[k].split(kw) if e != '']
                if len(tokens) == 0:
                    res.append([":"+kw, []])
                    k += 1
                    continue
                exprAndStmt = tokens[0].split('\n')
                parentExpr = exprAndStmt[0].strip()
                parentExprRes = self.deriveExpression(parentExpr)
                if parentExprRes == None:
                    return None
                res = [":"+kw, parentExprRes, []]
                k += 1
        return res

        
    def priority(self, c):
        if c == '^':
            return 4
        elif c == '*' or c == '/':
            return 3
        elif c == '+' or c == '-':
            return 2
        elif c in self.lexer.argOperators:
            return 1
        return 0

    
    def getOperatorToSplit(self, arg):
        res = None
        stk = []
        i = 0
        while i < len(arg):
            cur = arg[i]
            if isBelongToIdentifier(cur) or checkDigit(cur):
                idx = i + 1
                while idx < len(arg) and (self.lexer.checkValidIndentifier(cur+arg[idx]) or self.lexer.checkValidInteger(cur+arg[idx]) or self.lexer.checkValidFloat(cur+arg[idx])):
                    cur += arg[idx]
                    idx += 1
                i = idx
            elif cur == '(':
                stk.append((cur, i))
                i += 1
            elif cur == ')':
                while len(stk) > 0 and stk[-1][0] != '(':
                    res = stk.pop(-1)
                if(len(stk) > 0):
                    stk.pop(-1)
                i += 1
            elif cur in self.lexer.argOperators:
                idx = i + 1
                while idx < len(arg) and (cur+arg[idx]) in self.lexer.argOperators:
                    cur += arg[idx]
                    idx += 1
                while len(stk) > 0 and self.priority(stk[-1][0]) >= self.priority(cur):
                    res = stk.pop(-1)
                stk.append((cur, i))
                i = idx
            else:
                i += 1
        while len(stk) > 0:
            tmp = stk.pop(-1)
            if (tmp[0] != '(' and tmp[0] != ')'):
                res = tmp
        # return (op, pos_of_op)
        print(res)
        return res
                    

            
