#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i != 100):
            print("FizzBuzz" if not i % 3 and not i % 5 else "Fizz" if not i % 3
                    else "Buzz" if not i % 5 else i, end=" ")
		else:
			 print("Buzz")
