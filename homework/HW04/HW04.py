import re

def malayzator(text1, text2):
    with open(text1, "r", encoding="utf-8") as f:
        with open(text2, "w", encoding="utf-8") as f2:
            for line in f.readlines():
                line = (re.sub(r'Финлянди([яию(ей)])', r'Малайзи\1', line))
                line = (re.sub('Финля́ндия', 'Малайзия', line))
                f2.write(line)
                
def kebabter(text1, text2):
    with open(text1, "r", encoding="utf-8") as f:
        with open(text2, "w", encoding="utf-8") as f2:
            for line in f.readlines():
                line = (re.sub(r'язык([ауеи(ом)(ам)(ах)(ов)])\b', r'шашлык\1', line))
                line = (re.sub(r'Язык([ауеи(ом)(ам)(ах)(ов)]\b)', r'Шашлык\1', line))
                line = (re.sub('язык\b', r'шашлык', line))  
                line = (re.sub('Язык\b', r'Шашлык', line))
                f2.write(line)

def astrologizator(text1, text2):
    with open(text1, "r", encoding="utf-8") as f:
        with open(text2, "w", encoding="utf-8") as f2:
            for line in f.readlines():
                line = (re.sub(r'философи([яиюй(ей)(ям)(ях)])', r'астрологи\1', line))
                line = (re.sub(r'Философи([яиюй(ей)(ям)(ях)])', r'Астрологи\1', line))
                line = (re.sub('ФИЛОСОФИЯ','АСТРОЛОГИЯ', line))
                line = (re.sub('Филосо́фия','Астрология', line))
                f2.write(line)

malayzator("finland.txt", "malland.txt")
astrologizator("philosophy.txt", "astrosophy.txt")
kebabter("linguistics.txt", "shashlykstics.txt") 

























