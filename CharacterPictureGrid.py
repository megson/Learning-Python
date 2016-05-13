# Practice Program Question page-103

import sys

grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]

i=0
j=0

print(len(grid[0]))
print(len(grid))

for j in range(len(grid[0])):
    print('')
   # print('j= '+str(j))
    for i in range(len(grid)): # why did it not take 9?
          #  print('i= '+str(i))
            sys.stdout.write(grid[i][j])
