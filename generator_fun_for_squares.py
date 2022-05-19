# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
  for i in range(1,11):
    yield i*i		

# Driver code to check above generator function
for value in simpleGeneratorFun():
	print(value)