
class Token:
    def __init__(self,type,value):
        self.type=type#we would pass these 2 things to the object->Token(Integer,3)
        self.value=value
        print("type :" + str(self.type))
    def __str__(self):
        #after writing this you can access directly by writing obj.type or object.value
        return "Token({type},{value})".format(type=self.type,value=self.value)#just what it would print when asked to
    def __repr__(self):
        return self.__str__()

class Lexer:
    def __init__(self,text):
        self.text=text
        self.pos=0
        self.current_char = self.text[self.pos]

    def error(self):
        #generates the error message
        raise Exception("Invalid character")

    def advance(self):
        self.pos+=1
        if self.pos>len(self.text)-1:
            self.current_char=None
        else:
            self.current_char=self.text[self.pos]

    def escape_space(self):
        #helps in escaping spaces
        if self.current_char==" ":
            print("space escaped")
            self.advance()
            self.escape_space()
        #self.advance()
        #if we don't get any spaces then we just return he result
        return None

    def total_integer(self):
        result=""
        if self.current_char==None:
            return result
        if self.current_char.isdigit():
            result+=self.current_char
            self.advance()
            #we did call the recursion after increasing the position by 1, so that it takes the new character
            result+=self.total_integer()
        return result

    def get_next_token(self):
        self.escape_space()

        if self.current_char==None:
            return Token("EOF",None)

        if self.current_char>="0" and self.current_char<="9":
            token=Token("Integer",int(self.total_integer()))
            return token

        if self.current_char=="+":
            token=Token("Plus",self.current_char)
            self.advance()
            return token

        if self.current_char=="-":
            token=Token("Minus",self.current_char)
            self.advance()
            return token

        if self.current_char=="*":
            token=Token("Multiply",self.current_char)
            self.advance()
            return token

        if self.current_char=="/":
            token=Token("Divide",self.current_char)
            self.advance()
            return token

        if self.current_char=="(":
            token=Token("Lbracket",self.current_char)
            self.advance()
            return token

        if self.current_char==")":
            token=Token("Rbracket",self.current_char)
            self.advance()
            return token

        return self.error()

class AST:
    pass

class Binop(AST):
    def __init__(self,left,op,right):
        #print("In Binop " + str(op) +"left is "+str(left)+" right is "+str(right))
        self.left=left
        self.token=op
        self.op=op
        self.right=right

class Num(AST):
    def __init__(self,token):
        #print("In Num "+str(token))
        self.token=token
        self.value=token.value


class Parser:
    def __init__(self,lexer):
        self.lexer=lexer
        self.current_token=self.lexer.get_next_token()

    def error(self):
        #generates the error message
        raise Exception("Invalid syntax")


    def match(self,token_type):
        if self.current_token.type==token_type:
            self.current_token=self.lexer.get_next_token()
        else:
            self.error()

    def divfactor(self):
        #print("divfactor ->")
        token = self.current_token
        if token.type=="Integer":
            self.match("Integer")
            return Num(token)

        if token.type=="Lbracket":
            self.match("Lbracket")
            node=self.expression()
            self.match("Rbracket")
            return node

    def factor(self):
        #print("factor ->")
        node = self.divfactor()

        while self.current_token.type == "Divide":
            op=self.current_token
            self.match("Divide")
            node=Binop(left=node,op=op,right=self.divfactor())

        #print("End Factor")

        return node

    def term(self):
        #print("Term ->")
        node=self.factor()

        while self.current_token.type=="Multiply":
            op=self.current_token
            self.match("Multiply")
            node = Binop(left=node, op=op, right=self.factor())

        #print("End Term")

        return node

    def expression(self):
        #taking the first character
        #print("Expression ->")
        node=self.term()
        #now every time match is calling the get next token
        while self.current_token.type in ("Plus","Minus"):
            op=self.current_token

            if op.value=="+":
                self.match("Plus")
                node = Binop(left=node,op=op, right=self.term())
            elif op.value=="-":
                self.match("Minus")
                node = Binop(left=node, op=op, right=self.term())
            else:
                self.error()
        #print("End Expression ->")
        return node

    def parse(self):
        return self.expression()


class Interpreter():
    def __init__(self,parser):
        self.parser=parser

    def visit(self,node):
        if type(node).__name__ == "Binop":
            return self.visit_Binop(node)
        elif type(node).__name__ == "Num":
            return self.visit_Num(node)
        else:
            raise Exception("no visit method of this kind of node")


    def visit_Binop(self,node):
        if node.op.type=="Plus":
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type=="Minus":
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type=="Multiply":
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type=="Divide":
            return self.visit(node.left) / self.visit(node.right)
        else:
            #This situation wont come still writing
            raise Exception("No such binary operation defined :(")

    def visit_Num(self,node):
        return node.value

    def inter(self):
        tree=self.parser.parse()
        return self.visit(tree)

def main():
    while 1:
        try:
            inp=input("enter->")
        except EOFError:
            print("error occured")
            break
        if inp.lower()=="end":
            print("Thankyou for using Pinterpreter")
            break
        if not inp:
            continue

        lexer=Lexer(inp)
        parser=Parser(lexer)
        interp=Interpreter(parser)
        result=interp.inter()
        print(result)
        print("If you want to end type\"end\" in the input without quotes")

if __name__=="__main__":
    main()
