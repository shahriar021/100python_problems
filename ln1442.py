import re
email= input()
pa2="(\w+)@(\w+)\.(com)"
r2=re.match(pa2,email)
print(r2.group(2))
'''

emailAddress = input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2, emailAddress)
print (r2.group(2))
'''