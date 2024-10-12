with open('raw_data.bin', 'wb') as fh:
    fh.write(b'Hello world!')

s = b"Hello!"
print(s[1])


byte_str = 'some text'.encode()
print(byte_str)

numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)

for num in [127, 255, 156]:
    print(hex(num))

s = "Привіт!"
utf8 = s.encode()
print(f'UTF-8: {utf8}')
utf16 = s.encode("utf-16")
print(f'UTF-16: {utf16}')
cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")
s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s)


byte_array = bytearray(b"Kill Bill")
byte_array[0] = ord('B')
byte_array[5] = ord('K')
print(byte_array)


byte_array = bytearray(b"Hello")
byte_array.append(ord('!'))
print(byte_array)


byte_array = bytearray(b"Hello World")
string = byte_array.decode("utf-8")
print(string)

string1 = "Hello World"
string2 = "hello world"
if string1.lower() == string2.lower():
    print("Рядки однакові")
else: 
    print("Рядки різні")


german_word = "straße"
search_word = "STRASSE"
lower_comparison = german_word.lower() == search_word.lower()
casefold_comparison = german_word.casefold() == search_word.casefold()
print(f"Порівняння з lower(): {lower_comparison}")
print(f"Порівняння з casefold(): {casefold_comparison}")