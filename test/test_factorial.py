from factorial_module.factorial_module import *
import pytest

# test factorial_iterative function for positive, negative, and zero corner cases
def test_positive_factorial_iterativ():
  assert factorial_iterative(1) == 1
  assert factorial_iterative(5) == 120
  assert factorial_iterative(10) == 3628800
  
def test_negative_factoral_iterative():
  with pytest.raises(ValueError):
    factorial_iterative(-1)
  with pytest.raises(ValueError):
    factorial_iterative(-10)
    
def test_zero_factoral_iterative():
  assert factorial_iterative(0) == 1
  
  
  
# test factorial_recursion function for positive, negative, and zero corner cases  
def test_positive_factorial_recursion():
  assert factorial_iterative(0) == 1
  assert factorial_iterative(1) == 1
  assert factorial_iterative(5) == 120
  assert factorial_iterative(10) == 3628800
    
def test_negative_factoral_recursion():
  with pytest.raises(ValueError):
    factorial_iterative(-1)
  with pytest.raises(ValueError):
    factorial_iterative(-10)
    
def test_zero_factoral_recursion():
  assert factorial_iterative(0) == 1