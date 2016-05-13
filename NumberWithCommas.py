import re

#regex=re.compile(r'^((\d){1,3}\,)*(\d){1,3}$|^(\d){1,3}$')
regex2=re.compile(r'^\d{1,3}(,\d{3})*$')
#regex3=re.compile(r'(\S)?(?=.)(0|([1-9](\d*|\d{0,2}(,\d{3})*)))?(\S)?')
mo=regex2.search('333,333,333,333,333,333,333,347,425')
print(mo.group())
