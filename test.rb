require 'ripper'
require 'pp'

$_ = 9
# pp Ripper.lex("@@x22_>+--++1?'foo':'bar'")
code = '''
if ((x < 5) and (y > 8))+4
	x = x - 2
	y = y + 1
elsif x > 4
	z = x * 2
else
	y = y / 2
end
'''
pp Ripper.sexp(code)
