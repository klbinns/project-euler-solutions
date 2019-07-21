'''
Find the maximum total from top to bottom of the triangle contained in the input file
'''
filepath = 'p067_triangle.txt'  

# load input
triangle = []
with open(filepath) as fp:  
  line = fp.readline()
  while line:
    triangle.append([int(x) for x in line.split(" ")])
    line = fp.readline()


ind = len(triangle) - 1
while ind >= 1:
  cur_ind = ind
  next_ind = ind - 1

  curLine = triangle[cur_ind]
  nextLine = triangle[next_ind]

  mappedNextLine = []
  for idx, x in enumerate(nextLine):
    maxVal = max(curLine[idx], curLine[idx+1])
    mappedNextLine.append(x + maxVal)
  
  triangle[next_ind] = mappedNextLine
  ind -= 1

print(triangle[0][0])
