

#еще не решена проблема сохранения формата
#еще не решена проблема проверки ввода на некириллический алфавит и прочие знаки

text = input("Введите предложение кириллицей: ").lower()


d = {}
alpha = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
cifre = alpha[1::]+alpha[:1:]
for indx, letter in enumerate(alpha):
    d[letter] = cifre[int(indx)]

    
words = text.split()
new_words = []
for word in words:
    word_cifre = [d[let] for let in word.strip("!?:;,.)(")]
    new_words.append("".join(word_cifre))

if len(new_words)>1:
    new_words[-1], new_words[-2] = new_words[-2], new_words[-1]
    
print (" ".join(new_words))

























