import mymodule
print(mymodule.say_hello("World"))

#or

from mymodule import say_hello
print(say_hello("World"))

#or

from mymodule import say_hello as greeting
print(greeting("World"))

print(dir())

from mymodule2 import say_hello as greeting
print(greeting("World")) 