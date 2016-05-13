# Practice Question page-102

import sys
def convertToString(lisst):
    length=len(lisst)
    i=0
    for i in range(int(length)-1):
        sys.stdout.write(str(lisst[i])+', ')
    else:
        sys.stdout.write('and '+str(lisst[-1]))
    


spam=['apples','bananas','tofu','cats']

convertToString(spam)
    
    














