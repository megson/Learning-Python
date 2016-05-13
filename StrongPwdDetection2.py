import re
pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
password = input("Enter string to test: ")
result = re.findall(pattern, password)
if (result!=None):
    print ('Valid password')
else:
    print ('Password not valid')


import re
password = raw_input("Enter string to test: ")
if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
    # match
else:
    # no match
