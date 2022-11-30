''' exmaple module with a few math functions '''
def square(n):
  ''' returns the square of the parameter '''
  return n*n
  
def cube(n):
  return n*n*n

def test_square():
  assert square(4)==16
  assert square(-2)==4

def test_cube():
  assert cube(5)==125
  assert cube(-2)==-8

