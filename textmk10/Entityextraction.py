
'''
    Extraire des entités à partir d'un seul fichier.
     Le module retourne des groupes de noms et d'adjectifs à partir d'un texte.
'''

import os           #
import csv          #
import datetime     #
import nltk         #


THISDATE = str(datetime.date.today())

FILELOCATION = r"test.md"
OUTPUTLOCATION = r"extraction_entitées_{}.csv".format(THISDATE)

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


def extract_chunks(sent):
    '''Avec une phrase analysée, renvoyer des ensembles d'entités.'''
    grammar = r"""
    NBAR:
        # Noms et Adjectifs, terminer avec noms
        {<NN.*>*<NN.*>}
    NP:
        {<NBAR>}
        # Above, connected with in/of/etc...
        {<NBAR><IN><NBAR>}
    """
    chunker = nltk.RegexpParser(grammar)
    ne = set()
    chunk = chunker.parse(nltk.pos_tag(nltk.word_tokenize(sent)))
    for tree in chunk.subtrees(filter=lambda t: t.label() == 'NP'):
        ne.add(' '.join([child[0] for child in tree.leaves()]))
    return ne


def get_text_from_file(path):
    '''Renvoie le texte d'un chemin de fichier texte'''
    textout = ""
    fh = open(path, "r", encoding="utf8")
    for line in fh:
        textout += line
    fh.close()
    return textout


def parse_sentences(incorpus):
    '''Prendre un corps de texte et renvoyer des phrases dans une liste.'''
    sentences = nltk.sent_tokenize(incorpus)
    return sentences


def extract_entities(inpath):
    '''Prener un texte de plusieurs phrases et retourner une liste d'entités uniques.'''
    corpus = get_text_from_file(inpath)
    breakdown = parse_sentences(corpus)
    entities = []
    for sent in breakdown:
        for i in extract_chunks(sent):
            entities.append(i)
    remove_dups = set(entities)
    entities = list(remove_dups)
    return entities



# application

def main():
    print("Extraction des entitées...")
    records = []
    records.append(["Term", "rép", "Provenance", "Date"])

    # analyser du fichier

    print("obtention du fichier ... {}".format(FILELOCATION))

    corpus = get_textfromfile(FILELOCATION)
    record_terms = extract_entities(FILELOCATION)
    for term in record_terms:
        # print(term)
        record = []
        record.append(term)
        record.append(corpus.count(term))
        record.append(FILELOCATION)
        record.append(THISDATE)
        records.append(record)

    # Generation d'un ficheir d'output au format CSV

    csvout = open(OUTPUTLOCATION, 'w', newline="")
    csvwrite = csv.writer(csvout)
    for r in records:
        csvwrite.writerow(r)
    csvout.close()

    print("Création du rapport: " + OUTPUTLOCATION)


if __name__ == "__main__":
    main()
