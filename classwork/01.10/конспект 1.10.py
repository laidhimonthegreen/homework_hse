



print (chr(1149))
print (ord("а"))
alph = [chr(x) for x in range(ord ("а"), ord("я")+1)]
print(alph)

#работа с файлами (текстовые и бинарные)
#16 бит кодируют один символ

#чтение и запись
f = open("file.txt")
#относительный путь для вложенной директории
"dir1/file.txt"
#абсолютный
r"С:\Users\student\file.txt"
"С:\\Users\\student\\file.txt"
#если есть обратный слэш то питон сходит с ума
s = "абс\"de"
\t - табуляция
#относительный
"../file.txt"
filename = "file.txt"
f = open(filename, "r", encoding = "utf-8")
