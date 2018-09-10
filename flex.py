

#как работать в новой ветке

while True:
    slovo = input("Введите слово для анализа, прилагательное мужского рода: ")
    if slovo:       
        if slovo.endswith("ый") or slovo.endswith ("ой") or slovo.endswith ("ий"):
            rezult = "именительный или винительный падеж"
        elif slovo.endswith ("его") or slovo.endswith ("ого"):
            rezult = "родительный падеж"
        elif slovo.endswith ("ому") or slovo.endswith ("ему"):
            rezult = "дательный падеж"
        elif slovo.endswith ("им") or slovo.endswith ("ым"):
            rezult = "творительный падеж"
        elif slovo.endswith ("ом") or slovo.endswith ("ем"):
            rezult = "предложный падеж"
        else:
            rezult = "анализ ничего не показал"
        print ("Результат анализа:", rezult)
    else:
        break
    
    


































