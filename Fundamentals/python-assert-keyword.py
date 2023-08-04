# https://www.w3schools.com/python/ref_keyword_assert.asp

#The assert keyword is used when debugging code. The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.

#How it works

x = 5

assert x < 4, 'x is not less than 5'

# when false it shows the assert error
# if true then nothing is displayed


example-1
x = "hello"
#if condition returns True, then nothing happens:
assert x == "hello"
#if condition returns False, AssertionError is raised:
assert x == "goodbye"
example-2
x = "hello"
#if condition returns False, AssertionError is raised:
assert x == "goodbye", "x should be 'hello'"
