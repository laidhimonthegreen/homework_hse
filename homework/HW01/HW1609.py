#блок первый
print ("=Это первая часть программы=")
slovo = input("Введите слово (кириллицей): ")
for indx, letter in enumerate(slovo):
    if (int(indx%2) != 0 and letter not in ["а", "к"]):
        print (letter)

#блок второй
print ("=Это вторая часть программы=")
n = int(input ("Сколько раз вы хотите написать слово? "))
while True:
    n -= 1
    slovo2 = input ("Напишите слово: ")
    print (slovo2)
    if slovo2 == "программирование":
        break
    if n == 0:
        break

#блок третий
print ("=Это третья часть программы=")
slovo3 = input ("Введите ещё какое-нибудь слово: ")
antislovo3 = slovo3[::-1] 
let_number = len(slovo3) 
n3 = 0
antin3 = 0
for letter3 in slovo3:
    n3+=1
    if n3 <= (let_number/2):
        print (letter3) 
for antiletter3 in antislovo3:
    antin3+=1
    if antin3 <= ((let_number//2)+1):
        print (antiletter3) 
        





























