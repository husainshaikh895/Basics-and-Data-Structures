#Husain Shaikh
#90 degree clockwise matrix rotation

'''
1 2 3                       7 4 1
4 5 6  rotate 90 degrees	8 5 2
7 8 9                       9 6 3
--------------------------------------------------
'''
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotated = [list(reversed(col)) for col in zip(*matrix)]

for row in rotated:
    print(*row)


for col in zip(*matrix):
    print(col)

