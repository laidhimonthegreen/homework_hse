


while True:
    slovo = input("Введите слово для анализа, прилагательное мужского рода: ")
    if slovo:       
        if slovo.endswith("ый") or slovo.endswith ("ой") or slovo.endswith ("ий"):
            print ("Нам кажется, это именительный или винительный падеж")
        elif slovo.endswith ("его") or slovo.endswith ("ого"):
            print ("Нам кажется, это родительный падеж")
        elif slovo.endswith ("ому") or slovo.endswith ("ему"):
            print ("Нам кажется, это дательный падеж")
        elif slovo.endswith ("им") or slovo.endswith ("ым"):
            print ("Нам кажется, это творительный падеж")
        elif slovo.endswith ("ом") or slovo.endswith ("ем"):
            print ("Нам кажется, это предложный падеж")
        else:
            print ("Мы ничего не понимаем")
    else:
        break
    
    


































