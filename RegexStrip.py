# Regex Version of strip() page 171

# functions takes string does same thing as strip string method
     # remove whitespace if only string is passed
     # if 2nd string passed remove those characters from the first string

import re


def option1(text):
    
   # text='  meghna  '
   # text2='mna'
    mo=re.search(r'(\s*)(\w+)(\s*)',text)
    if(mo.group(2)!=None):
        print(mo.group(2))

def option2(text,text2):
    reg=re.compile(r'[^'+text2+']')
    mo=reg.findall(text)
    print(''.join(mo))

print('Select your option:')
print('1. Enter 1 string from which the whitespaces would be removed')
print('2. Enter 1 string and a second string that you want to delete from the first')

option=input()

if(int(option)==1):
    print('Enter your 1 and only String')
    text=input()
    option1(text)
    elif(int(option)==2):
        print('Enter your 1st String')
        text=input()
        print('Enter your 2nd String')
        text2=input()
        option2(text,text2)
    else:
        print('what??')
