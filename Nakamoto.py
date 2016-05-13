import re

regex=re.compile(r'^[A-Z][a-z]*\sNakamoto$')
mo=regex.search('Q Nakamoto')
print(mo.group())
