cars = ["mustang", "jeep", "porshe"]
print(len(cars))

#add a car
print(cars.append("ferrari"))
print(cars)
#print(len(cars))

(cars.remove("ferrari"))
print(cars)

(cars.pop(1))
print(f"there are {len(cars)} cars")


greeting = "Hello"
print(greeting[0])

print(greeting.lower())
print(greeting.upper())

print(input("what is your name? ") .lower())
print(input("what is your name? ") .upper())

"anything".lower()

# split and join
hello = "helo my name is josh" .split(" ")
print(hello)
hello.pop()
print(hello)
hello.append("Steve")

hello = " " .join(hello)

print(hello)






