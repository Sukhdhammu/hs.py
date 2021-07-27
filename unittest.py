def add(n1, n2) :
  return n1 + n2

def test_add():
  assert add(2, 3) == 5
  assert add ('space', 'ship') == 'spaceship'
  
  def subtract(n1, n2):
    return n1+ n2 # <---fix this in step 7
  
  # uncomment the following test in step 5
  #def test_subtract():
  #   assert subtract(2, 3) == -1
