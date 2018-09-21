


while True:
    sentence = input("Введите предложение для анализа: ")
    s = sentence.split()
    print (s)
    for slovo in s:
        slovo1 = slovo.strip("!?,.:;")
        print (slovo1)
        if slovo1.endswith("ый") or slovo1.endswith ("ой") or slovo1.endswith ("ий"):
            rezult = "именительный или винительный падеж"
        elif slovo1.endswith ("его") or slovo1.endswith ("ого"):
            rezult = "родительный падеж"
        elif slovo1.endswith ("ому") or slovo1.endswith ("ему"):
            rezult = "дательный падеж"
        elif slovo1.endswith ("им") or slovo1.endswith ("ым"):
            rezult = "творительный падеж"
        elif slovo1.endswith ("ом") or slovo1.endswith ("ем"):
            rezult = "предложный падеж"
        else:
            rezult = "извините, пока программа анализирует только прилагательные м.р. ед.ч."
        print ("Результат анализа:", rezult)
    else:
        break
    




























