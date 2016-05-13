import sys

eoff=False

sys.stdin.readline()
try:
    while eoff==False:
        print(eoff)
        line=sys.stdin.readline()
        
        if None=='\n':
             print(line) 
        else:
            eoff=True
    else:
        print('eof became true')
        sys.exit()
        

except Exception as e: print(str(e))
