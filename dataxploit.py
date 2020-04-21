from os import listdir
from os.path import join, isfile

directorypy = r'/root/Documents/ARSENAL/SENTINEL/STRATOS/test/'
directorymat =  r'/root/Documents/ARSENAL/SENTINEL/STRATOS/test/'

list_cmp = [] # contiendra les fichiers identiques

for files in listdir(directorypy) : # pour tous les fichiers du répertoire
    pathpy = join(directorypy, files) # on joint le répertoire et le fichier
    pathmat = join(directorymat, files) # on joint le répertoire et le fichier
    if isfile(pathpy): # si c'est un fichier
        if isfile(pathmat):
            if isfile(pathpy):
             mat = open(pathpy)
             py = open(pathmat)
             linemat= mat.read()
             linepy = py.read()

             for x in xrange(min(len(linemat),len(linepy))):
                  if linemat[x]!=linepy[x]:
                      print("Les deux fichiers sont differents")
             else:
                  if linemat[x] == linepy[x] :
                      print("les fichiers sont identiques")
