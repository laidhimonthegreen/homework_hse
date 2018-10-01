
"""В данной программе шифр Цезаря работает только для кириллических букв;
Все пробелы, знаки препинания, цифры остаются на прежнем месте;
Формат сохраняется."""


#создание словарей
d = {}
alpha = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alpha_cap = alpha.upper()

cifre = alpha[1::]+alpha[:1:]
cifre_cap = alpha_cap[1::]+alpha_cap[:1:]

for indx, letter in enumerate(alpha):
    d[letter] = cifre[indx]
for indx, letter in enumerate(alpha_cap):
    d[letter] = cifre_cap[indx]


text = input("Введите предложение кириллицей: ")

#проверяем, можно ли что-то зашифровать   
n = 0
for i in text:
    if i in alpha+alpha_cap:
        n+=1

if n == 0:
    print ("Кажется, здесь нет ничего кириллического для зашифровки")
else:
    #сдвигаем кириллические знаки, не сдвигаем другие знаки
    letters = [d[let] if let in d else let for let in text]

    text2 = ("".join(letters))
    
    words = text2.split()

    #сохраняем знаки пунктуации на месте при перестановке слов
    znak1, znak2 = "", ""
    if len(words)>1:      
        if words[-1][-1] in ("!?:;.,)("):
            znak1 = words[-1][-1]
        if words[-2][-1] in ("!?:;.,)("):
            znak2 = words[-2][-1] 
        
        words[-1], words[-2] = words[-2].strip("!?:;.,)(")+znak1, words[-1].strip("!?:;.,)(")+znak2
        

    print(" ".join(words))
 






















