'''
import re
emailAddress = input()
p= "(\w+)@((\w\.)+(com))"
r=re.match(p,emailAddress)
print( r.group(1))
'''
import re
emailAddress = input()
pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2, emailAddress)
print (r2.group(1))
