#python tuples
tuple = ("table", "jug", "shoes", "cherry", "jug")
print(tuple)
print(len(tuple))
print(type(tuple))
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
#tuple2 = tuple(("apple", "banana", "grape"))
#print(tuple2)
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
x = lambda a : a + 10
print(x(5))
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))