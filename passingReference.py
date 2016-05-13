#page 100 

def eggs(someParameter):
    someParameter.append('Hello')

spam=[1,2,3]
eggs(spam)
print(spam)
print('---------------')

#copy.copy() --> page 101

import copy

spam=['A','B','C','D']
cheese=copy.copy(spam)
cheese[1]=42
print('spam(not changed v=because of cheese)')
print(spam)
print('cheese')
print(cheese)
print('---------------')

#copy.deepcopy() --> page 101
# deepcopy is used to copy innerLists if there

#import copy

spam=['A','B','C','D']
dcheese=copy.deepcopy(spam)
dcheese[1]=42
print(spam)
print(dcheese)
