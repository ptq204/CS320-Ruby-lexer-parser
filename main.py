import re
from mparser import *
from mlexer import *

# if re.match(r'.+ while .+', "x = x + 1 if x < 10 while k == 0"):
#     print('MATCH')
# else:
#     print('NO MATCH')

lex = Lexer()
par = Parser(lex)

code = "x = x + 1 if x < 10 while y < 5"

code = '''
while x > 5
	x = 1
	y = x - 1
end
'''

code = '''
if x < 5
	x = x - 2
	y = y + 1
elsif x > 4
	z = x * 2
else
	y = y / 2
end
'''
pattern = r'while(.+\n)*end'
if re.match(pattern, code.strip('\n')):
	print('MATCH')
else:
	print('NOT MATCH')
print(par.parseCode(code.strip('\n')))
