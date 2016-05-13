import sys

def collatz(number):
    if(number%2==0):
        print(number//2)
        return number//2
    else:
        print(3*int(number)+1)
        return 3*int(number)+1

no=1
print('Enter Number')
while no>0:
    num=input()
    ans=collatz(int(num))
    if(ans==1):
        sys.exit()
    
