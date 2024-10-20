'''
В нас є список зі слів, потрібно написати функцію, яка буде брати кожне слово і обрізати до певної довжини
'''

word_list = [
    "Hippopotomonstrosesquippedaliophobia", # Hipp...
    "Pneumonoultramicroscopicsilicovolcanoconiosis",
    "Supercalifragilisticexpialidocious"
]

def shorten_word_list(words: list[str], word_length: int) -> list[str]:
    result = []
    for word in word_list:
        result.append(shorten_word(word, word_length))
    return result

def shorten_word_list_alternative(word_list: list[str], word_length: int) -> list[str]:
    return [shorten_word(word, word_length) for word in word_list] 

def shorten_word(word: str, word_length: int) -> str:
    return f"{word[0:word_length]}..." 

print(shorten_word(word_list[0], 4))
print(shorten_word_list(word_list, 3))
print(shorten_word_list_alternative(word_list, 3)) 