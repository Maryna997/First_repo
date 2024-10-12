fh = open("test.txt", "w")
symbols_written = fh.write("hello!")
fh.close()

fh = open ("tst.txt", "w+")
fh.write("hello!")
fh.seek(0)

first_two_symbols = fh.read(2)
print(first_two_symbols)
fh.close()

fh = open("test.txt", "w")
fh.write("hello!")
fh.close

fh = open("test.txt", "r")
all_file = fh.read()
print(all_file)

fh.close()

fh = open("test.txt", "r")
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol)

fh.close() 

fh = open("test.txt", "w")
fh.write("first line\nsecond line\nthird line")
fh.close()

fh = open("test.txt", "r")
while True: 
    line = fh.readline()
    if not line:
        break
    print(line)

fh.close()


fh = open("test.txt", "r")
lines = fh.readlines()
print(lines)

fh.close()

fh = open('test.txt', 'r')
lines = [el.strip() for el in fh.readlines()]
print(lines)

fh.close()

fh = open("test.txt", "w+")
fh.write("hello!")
fh.seek(1)
second = fh.read(1)
print(second)
fh.close()

fh = open("test.text", "w+")
fh.write("hello!")
position = fh.tell()
print(position)
fh.seek(1)
position = fh.tell()
print(position)
fh.read(2)
position = fh.tell()
print(position)
fh.close()


fh = open('test.txt', 'w')
try:
    fh.write("Some data")
finally:
    fh.close() 


with open("test.txt", "w") as fh:
    fh.write("first line\nsecond line\nthird line")

with open("test.txt", "r") as fh:
    lines = [el.strip() for el in fh.readlines()]
print(lines)