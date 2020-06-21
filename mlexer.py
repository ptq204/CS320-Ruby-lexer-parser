from menum import *
from utils import *

class Lexer:
    def __init__(self):
        self.transition_table_indentifier = [
            [STATE1, STATE3, END_STATE, N_],
            [N_, N_, END_STATE, N_],
            [N_, N_, END_STATE, END_STATE],
            [N_, STATE4, END_STATE, N_],
            [N_, N_, END_STATE, N_],
            [N_, N_, END_STATE, END_STATE]
        ]

        self.transition_table_integer = [
            [INT_STATE1, INT_END_STATE2, INT_END_STATE3, INT_END_STATE3],
            [INT_STATE1, INT_END_STATE4, INT_END_STATE5, INT_END_STATE5],
            [N_, INT_END_STATE2, INT_END_STATE2, N_],
            [N_, INT_END_STATE3, INT_END_STATE3, INT_END_STATE3],
            [N_, INT_END_STATE4, INT_END_STATE4, N_],
            [N_, INT_END_STATE5, INT_END_STATE5, INT_END_STATE5]
        ]

        self.transition_table_float = [
            [FLOAT_STATE1, FLOAT_STATE3, FLOAT_STATE2, N_],
            [FLOAT_STATE1, FLOAT_STATE3, FLOAT_STATE2, N_],
            [N_, FLOAT_STATE2, FLOAT_STATE2, FLOAT_STATE4],
            [N_, N_, N_, FLOAT_STATE4],
            [N_, FLOAT_END_STATE, FLOAT_END_STATE, N_],
            [N_, FLOAT_END_STATE, FLOAT_END_STATE, N_]
        ]

        self.keywords = ["if", "else", "elsif", "until", "for", "while", "unless", "do", "then", "end", "nil", "self"]
        self.stmtKeywords = ["if", "while", "until"]
        self.exprKeywords = ["and", "or", "not"]
        self.argOperators = [">", ">=", "<", "<=", "==", "===", "!=", "=", "+", "-", "*", "/", "%", "**", ">>", "<<", "&&", "||", "+=", "-=", "*=", "/="]

    def checkValidIndentifier(self, identifier):
        if identifier in self.keywords:
            return False
        state = START_STATE
        for c in identifier:
            if c == '$':
                state = self.transition_table_indentifier[state][DOLLAR]
            elif c == '@':
                state = self.transition_table_indentifier[state][AT]
            elif checkLetter(c):
                state = self.transition_table_indentifier[state][LETTER]
            elif checkDigit(c):
                state = self.transition_table_indentifier[state][DIGIT]
            else:
                return False
            if state == N_:
                return False
        return state == END_STATE


    def checkValidInteger(self, number):
        state = INT_START_STATE
        for c in number:
            if c == '+' or c == '-':
                state = self.transition_table_integer[state][ADD_MINUS]
            elif c == '0':
                state = self.transition_table_integer[state][ZERO]
            elif checkNumberOneToSeven(c):
                state = self.transition_table_integer[state][ONE_TO_SEVEN]
            elif c =='8' or c == '9':
                state = self.transition_table_integer[state][EIGHT_TO_NINE]
            else:
                return False
            if state == N_:
                return False
        return state == INT_END_STATE2 or state == INT_END_STATE3 or state == INT_END_STATE4 or state == INT_END_STATE5


    def checkValidFloat(self, number):
        state = FLOAT_START_STATE
        for c in number:
            if c == '+' or c == '-':
                state = self.transition_table_float[state][ADD_MINUS]
            elif c == '0':
                state = self.transition_table_float[state][ZERO]
            elif checkPositiveNumber(c):
                state = self.transition_table_float[state][FONE_TO_NINE]
            elif c == '.':
                state = self.transition_table_float[state][FDOT]
            else:
                return False
            if state == N_:
                return False
        return state == FLOAT_END_STATE


    def tokenize(self, code):
        pos = 0
        token_list = []
        while pos < len(code):
            if isSpace(code[pos]):
                pos += 1
                continue
            if isOperator(code[pos]):
                if code[pos] == '+':
                    token_list.append(["ADD:", code[pos]])
                elif code[pos] == '-':
                    token_list.append(["SUB:", code[pos]])
                elif code[pos] == '*':
                    token_list.append(["MUL:", code[pos]])
                elif code[pos] == '/':
                    token_list.append(["DIV:", code[pos]])
                pos += 1
                continue
            if isBracket(code[pos]):
                if code[pos] == '(':
                    token_list.append(["LEFT-BRACKET:", code[pos]])
                else:
                    token_list.append(["RIGHT-BRACKET:", code[pos]])
                pos += 1
                continue
            i = pos
            currToken = ''
            while i < len(code):
                if isSpace(code[i]) or isOperator(code[i]) or isBracket(code[i]):
                    break
                currToken += code[i]
                i += 1
            if currToken in self.keywords:
                token_list.append([])
            if self.checkValidIndentifier(currToken):
                token_list.append(["IDENT:", currToken])
            elif self.checkValidInteger(currToken):
                token_list.append(["INT:", currToken])
            elif self.checkValidFloat(currToken):
                token_list.append(["FLOAT:", currToken])
            else:
                print('Error: Invalid code')
            pos = i
        return token_list

    
    def getAllKeyWords(self, code, keywords):
        pos = 0
        kw_list = []
        while pos < len(code):
            if isSpace(code[pos]) or isBracket(code[pos]):
                pos += 1
                continue
            i = pos
            tmp = i
            currToken = ''
            while i < len(code):
                if isSpace(code[i]) or isBracket(code[i]):
                    break
                currToken += code[i]
                i += 1
            if currToken in keywords:
                kw_list.append((tmp, currToken))
            pos = i
        return kw_list


# lexer = Lexer()
# print(lexer.checkValidIndentifier(input()))