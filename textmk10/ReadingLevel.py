'''
    Rapport de niveau de lecture
     Script pour mesurer le niveau de lecture d'un texte.
'''

import os

FILELOCATION = r"test.md"

def to_str(bytes_or_str):
    '''Convertir le fichier en UTF-8'''
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def get_textfromfile(path):
    '''Renvoyer le texte d'un chemin de nom de fichier'''
    textout = ""
    fh = open(path, "r", encoding="utf8")
    for line in fh:
        textout += line
    fh.close()
    textout = to_str(textout)
    return textout


def main():
    '''logique du script.'''

    text=get_textfromfile(FILELOCATION)

    sentence=text.count(".") + text.count('!') + text.count(";") + text.count(":") + text.count("?")

    words=len(text.split())
    syllable=0

    for word in text.split():
        for vowel in ['a','e','i','o','u']:
            syllable += word.count(vowel)
        for ending in ['és','é','ées','ée']:
            if word.endswith(ending):
                syllable -= 1
        if word.endswith('endre'):      #Ajouter d'autre contrainte
                syllable += 1

    G=round((0.39*words)/sentence+ (11.8*syllable)/words-15.59)     #

    if G >= 0 and G <=30:
        print('Score: {} lisabilité de niveau débutant'.format(G))
    elif  G >= 50 and G <=60:
        print('Score: {} lisabilité de niveau intermédiaire'.format(G))
    elif  G >= 90 and G <=100:
        print('Score: {} lisabilité de niveau avancé'.format(G))

    print('Le texte est composé de %d mots' %(words))

if __name__ == "__main__":
    main()
