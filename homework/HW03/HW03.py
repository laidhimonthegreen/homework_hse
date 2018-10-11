#это черновая версия программы
#надо: спросить про табуляцию, open with as




import random
 
#СЛОВА И СЛОВОСОЧЕТАНИЯ
def sing_noun():
    sing_nouns = []
    f = open("sing_noun.tsv")
    sing_nouns = [word.strip() for word in f.readlines()]
    return random.choice(sing_nouns)

def adv():
    adverbs = []
    f = open("adv.tsv")
    adverbs = [word.strip() for word in f.readlines()]
    return random.choice(adverbs)

def intens(adv):
    intensifiers = []
    f = open("intensifier.tsv")
    intensifiers = [word.strip() for word in f.readlines()]
    result = random.choice(intensifiers) + " " + adv()
    return result

def plural_noun():
    plural_nouns = []
    f = open("plural_nouns.tsv")
    plural_nouns = [word.strip() for word in f.readlines()]
    return random.choice(plural_nouns)

def adj(plural_nouns):
    adjectives = []
    f = open("adj.tsv")
    adjectives = [word.strip() for word in f.readlines()]
    return random.choice(adjectives) + " " + plural_noun()

def verb():
    verbs = []
    f = open("verb.tsv")
    verbs = [word.strip() for word in f.readlines()]
    return random.choice(verbs)
  
def verbgroup():
    return adj(plural_noun()) + " " + verb() + " " + plural_noun()
 
#ПРЕДЛОЖЕНИЯ
#Hideous cats eat bats very often.
def random_usual():
    sentence_usual = (adj(plural_noun()) + " " + verb() + " " + plural_noun() + " "
                + intens(adv) + ".")
    return sentence_usual.capitalize() 
 
#Do hideous cats eat bats very often?
def random_question():
    sentence_question = ("Do" + " " + verbgroup() + " " + intens(adv) + "?")
    return sentence_question

#Hideous cats do not eat bats very often.
def random_not():
    sentence_not = (adj(plural_noun()) + " " + "do" + " " + "not" + " " + verb()
                + " " + plural_noun() + " " + intens(adv) + ".")
    return sentence_not.capitalize() 
 

#If awesome cats eat bats, stupid bats eat cats.
def random_if():
    sentence_if = ("If" + " " + verbgroup() + "," + " " + verbgroup() + ".")
    return sentence_if
 
#Cat, eat hideous bats!
def random_order():
    sentence_order = (sing_noun() + "," + " " + verb() + " "
                + adj(plural_noun()) + "!")
    return sentence_order.capitalize() 

def write_sentences():
    sentences = [random_usual(), random_question(), random_if(),
             random_order(), random_not()]

    random.shuffle(sentences)
    text = open("text.txt", "w")
    text.write(" ".join(sentences))
    text.close()


def main():
    write_sentences()
    return 0

 
if __name__ == '__main__':
    main()
 
