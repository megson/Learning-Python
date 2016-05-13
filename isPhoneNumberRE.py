import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#find 1 number
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

#find all occurances- returns a list
print(phoneNumRegex.findall('Call me on 415-555-4242 or 415-365-4342'))


# you can also get the number in groups by putting paranthesis
phoneNum2Regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo2 = phoneNum2Regex.search('My number is 415-555-4242.')
mo2.group()
print('---------')
print(mo2.group(1))
print(mo2.group(2))
print(mo2.group(3))

#to search for number with parenthesis use a backslash before it
phoneNum3Regex = re.compile(r'(\(\d\d\d\)) \d\d\d-\d\d\d\d')
mo3 = phoneNum3Regex.search('My number is (415) 555-4242.')
print(mo3.group())

# to search for words starting with similar word
batRegex= re.compile(r'Bat(man|mobile|copter)')
mo4=batRegex.search('Batman got hit by a Bat')
print(mo4.group())
mo5=batRegex.search('Batmotorcycle got hit by a Bat')
print(mo5==None)

#
bat2Regex=re.compile(r'Bat(wo)?man') # wo can appera 1 or 0 times--> ?
mo6=bat2Regex.search('The Adventure of Batman') # it is case-sensitive b!=B
print(mo6.group())

# for 1 or more times use --> +
bat2Regex=re.compile(r'Bat(wo)*man') # wo can appera 0 or more times--> *
mo6=bat2Regex.search('The Adventure of Batwowowowoman') # it is case-sensitive b!=B
print(mo6.group())

#
phoneNum4Regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo7 = phoneNum4Regex.search('My number is 415-555-4242.')
print(mo7.group())
mo7 = phoneNum4Regex.search('My number is 555-4242.')
print(mo7.group())

#
bat2Regex=re.compile(r'(hahaha(,)?){3}') # hahaha appears exactly 3 times with COMMA
mo6=bat2Regex.search('hahaha,hahaha,hahaha') 
print(mo6.group())

# you can also write {,5}-> 0 to 5 || {3,}--> 3 or mmore than three
bat2Regex=re.compile(r'(ha){3,5}') # ha appears between a range of 3 and 5
mo6=bat2Regex.search('hahaha,hahaha,hahaha') 
print(mo6.group())

# 
bat2Regex=re.compile(r'(\d){3,5}') 
mo6=bat2Regex.search('12345678') 
print(mo6.group())
