from collections import Counter

text= "missisipi"
# res = {}
# for char in text:
#     if char in res:
#         res[char] += 1
#     else:
#         res[char] = 1
# print(res)

count = Counter(text)
print(type(count)) 
print(count)


text = "missiSipi"
count = Counter(text.lower())
print(count)
print(count.most_common(3))

# to have dictionary:
count = dict(Counter(text.lower()))
print(count) 


text = "To be or not to be"
words = text.lower().split()
print(words)
count = Counter(words)
print(count)