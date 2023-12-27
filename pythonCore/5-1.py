one_line_text = "Textual data in Python is handled with str objects, or strings. "\
                "Strings are immutable sequences of Unicode code points. "\
                "String literals are written in a variety of ways: single quotes, double quotes, triple quoted."
print(one_line_text)

s = "Hi there!"

start = 0
end = 7

print(s.find("er", start, end)) # 5 індекс першого збігу
print(s.find("q"))  # -1 - послідовність не знайдена

'''Якщо вам потрібно здійснити пошук підрядка у рядку справа, а не зліва як у find, то для цього є метод rfind:'''

s = 'Some words'
s.rfind('o')  # 6

print(s.index("er", start, end)) # 5 індекс першого збігу
#print(s.index("q"))  # err - послідовність не знайдена - генерує помилку ValueError: substring not found

#І "правий" аналог index — rindex:

s = 'Some words'
s.rindex('o')  # 6

s = "I am learning strings in Python. Some new methods got now."
sentences = s.split(". ")

print(sentences[0]) # I am learning strings in Python
print(sentences[1]) # Some new methods got now.
#print(sentences[2]) # Some new methods got now.
sentences = ["I am learning strings in Python", "Some new methods got now."]
text = ". ".join(sentences)
print(text) # I am learning strings in Python. Some new methods got now.