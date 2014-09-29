# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def standard_list(n):
  p = []
  i = 1
  while i <= n:
    p.append(i)
    i += 1 
  return p

def compare_list(tocompare,p):
  for e in tocompare:
    if e not in p:
      return False
  return True

def row_to_col(rows):
  size = len(rows)
  cols = []
  i = 0
  while i < size:
    c=[]
    for e in rows:
      c.append(e[i])
    cols.append(c)
    i += 1
  return cols

def check_sudoku(square):
  size = len(square)
  for e in square:
    i = 0
    while i < size:
      if not compare_list(standard_list(size),square[i]):
        return False
      if not compare_list(standard_list(size),row_to_col(square)[i]):
        return False
      i +=1
  return True

    
print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False


