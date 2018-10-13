import random
 
#СЛОВА И СЛОВОСОЧЕТАНИЯ
def sing_noun(): 
    sing_nouns = []
    with open("sing_noun.tsv") as f: 
        for lin in f.readlines(): 
            listline = lin.split("\t") 
            for word in listline:
                if word.strip():
                    sing_nouns.append(word.strip()) 
        return random.choice(sing_nouns)
 
def adv(): 
    adverbs = []
    with open("adv.tsv") as f: 
        for lin in f.readlines(): 
            listline = lin.split("\t")
            for word in listline:
                if word.strip():
                    adverbs.append(word.strip()) 
    return random.choice(adverbs)


def intens(adv): 
    intensifiers = []
    with open("intensifier.tsv") as f: 
        for lin in f.readlines(): 
            listline = lin.split("\t")
            for word in listline:
                if word.strip():
                    intensifiers.append(word.strip()) 
        result = random.choice(intensifiers) + " " + adv()
    return result
 
     
def plural_noun(): 
    plural_nouns = []
    with open("plural_nouns.tsv") as f: 
        for lin in f.readlines(): 
            listline = lin.split("\t") 
            for word in listline:
                if word.strip():
                    plural_nouns.append(word.strip()) 
    return random.choice(plural_nouns)
    
def adj(plural_nouns): 
    adjectives = []
    with open("adj.tsv") as f: 
        for lin in f.readlines(): 
            listline = lin.split("\t") 
            for word in listline:
                if word.strip():
                    adjectives.append(word.strip()) 
    return random.choice(adjectives) + " " + plural_noun()

def verb(): 
    verbs = []
    with open("verb.tsv") as f: 
        for lin in f.readlines(): 
            listline = lin.split("\t") 
            for word in listline:
                if word.strip():
                    verbs.append(word.strip()) 
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
 
