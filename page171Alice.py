import re


#Regex=re.compile(r'\s Alice|Bob|Carol \s eats|pets|throws \s apples|cats|baseballs \.')
Regex=re.compile(r'(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.')
mo=Regex.search(' Alice eats apples.')
print(mo.group())
 
