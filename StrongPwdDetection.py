# strong password Detection 171 pg

import re

def Pass(text):
    
    output=True

    if(len(text)!=8):
        output=False
    if(re.search(r'[A-Z]',text)==None):
        output=False
    if(re.search(r'[a-z]',text)==None):
        output=False
    if(re.search(r'[0-9]',text)==None):
        output=False

    return output

print('Enter a password')
Text=input()
isStrong=Pass(Text)

if(isStrong):
    print('Gud Password')
else:
    print('Bad password')
    

