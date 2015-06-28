### Can you write a FizzBuzz algorithm? It goes like this:
### Loop through all the integers from 1 to 100
### If the number is divisible by 3, print "Fizz"
### If the number is divisible by 5, print "Buzz"
### If the number is divisible by both, print "FizzBuzz"
### If the number is divisible by neither, print the number

for i in range(1,100):
	if i % 15 == 0:
		print ("Fizz")
	elif i % 5 == 0:
		print ("Buzz")
	elif i % 3 == 0:
		print ("FizzBuzz")
	else:
		print (i)
		
		

